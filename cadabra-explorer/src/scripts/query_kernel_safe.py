import sys
import json
import jupyter_client

def query_kernel(connection_file, payload_json):
    try:
        payload = json.loads(payload_json)
        action = payload.get("action")
    except Exception as e:
        print(json.dumps({"error": f"Invalid JSON payload: {e}"}))
        return

    client = jupyter_client.BlockingKernelClient(connection_file=connection_file)
    client.load_connection_file()
    client.start_channels()

    if action == "list":
        code = """
import json
def __cadabra_explorer_query():
    result = []
    for name, val in list(globals().items()):
        if type(val).__name__ == 'Ex':
            item = {
                "name": name,
                "type": "Ex"
            }
            try:
                item["preview"] = str(val)
                item["latex"] = getattr(val, '_latex_', lambda: str(val))()
                item["inputForm"] = getattr(val, 'input_form', lambda: str(val))()
            except Exception:
                item["preview"] = ""
                item["latex"] = ""
                item["inputForm"] = ""
            result.append(item)
    return json.dumps(result)
print(__cadabra_explorer_query())
"""
    elif action == "inspect":
        variable = payload.get("variable")
        if not variable or not isinstance(variable, str) or not variable.isidentifier():
            print(json.dumps({"error": "Invalid variable name"}))
            client.stop_channels()
            return

        code = f"""
import json
def __cadabra_explorer_inspect():
    val = globals().get('{variable}')
    if val is None:
        return json.dumps({{"error": "Variable not found"}})
    elif type(val).__name__ != 'Ex':
        return json.dumps({{"error": "Not a Cadabra Ex object"}})
    else:
        try:
            latex_str = getattr(val, '_latex_', lambda: '')()
            ast_repr = repr(val)
            return json.dumps({{"latex": latex_str, "ast": ast_repr}})
        except Exception as e:
            return json.dumps({{"error": str(e)}})
print(__cadabra_explorer_inspect())
"""
    else:
        print(json.dumps({"error": "Unknown action"}))
        client.stop_channels()
        return

    msg_id = client.execute(code=code, silent=True, store_history=False)

    output = ""
    try:
        while True:
            msg = client.get_iopub_msg(timeout=2)
            
            # Ignore messages that don't belong to our execution request
            if msg.get('parent_header', {}).get('msg_id') != msg_id:
                continue
                
            if msg['msg_type'] == 'stream' and msg['content']['name'] == 'stdout':
                output += msg['content']['text']
            elif msg['msg_type'] == 'status' and msg['content']['execution_state'] == 'idle':
                break
    except Exception as e:
        output = json.dumps({"error": f"Timeout or IOPub error: {str(e)}"})

    client.stop_channels()
    print(output.strip())

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(json.dumps({"error": "Usage: python query_kernel_safe.py <connection_file> <json_payload>"}))
        sys.exit(1)

    query_kernel(sys.argv[1], sys.argv[2])
