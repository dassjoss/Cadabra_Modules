import * as vscode from 'vscode';

export class InspectorWebview {
    private static currentPanel: InspectorWebview | undefined;
    private readonly _panel: vscode.WebviewPanel;
    private readonly _extensionUri: vscode.Uri;
    private _disposables: vscode.Disposable[] = [];

    public static createOrShow(extensionUri: vscode.Uri, name: string, latex: string) {
        const column = vscode.window.activeTextEditor
            ? vscode.window.activeTextEditor.viewColumn
            : undefined;

        // If we already have a panel, show it and update the math
        if (InspectorWebview.currentPanel) {
            InspectorWebview.currentPanel._panel.reveal(column);
            InspectorWebview.currentPanel.updateContent(name, latex);
            return;
        }

        // Otherwise, create a new panel.
        const panel = vscode.window.createWebviewPanel(
            'cadabraInspector',
            'Cadabra Inspector',
            column || vscode.ViewColumn.One,
            {
                enableScripts: true,
                localResourceRoots: [vscode.Uri.joinPath(extensionUri, 'node_modules', 'katex', 'dist')]
            }
        );

        InspectorWebview.currentPanel = new InspectorWebview(panel, extensionUri, name, latex);
    }

    private constructor(panel: vscode.WebviewPanel, extensionUri: vscode.Uri, name: string, latex: string) {
        this._panel = panel;
        this._extensionUri = extensionUri;

        this.updateContent(name, latex);

        this._panel.onDidDispose(() => this.dispose(), null, this._disposables);
    }

    public updateContent(name: string, latex: string) {
        this._panel.title = `Inspector: ${name}`;
        this._panel.webview.html = this._getHtmlForWebview(this._panel.webview, name, latex);
    }

    public dispose() {
        InspectorWebview.currentPanel = undefined;

        this._panel.dispose();

        while (this._disposables.length) {
            const x = this._disposables.pop();
            if (x) {
                x.dispose();
            }
        }
    }

    private _getHtmlForWebview(webview: vscode.Webview, name: string, latex: string) {
        // Local path to KaTeX assets
        const katexUri = vscode.Uri.joinPath(this._extensionUri, 'node_modules', 'katex', 'dist');

        const katexCssUri = webview.asWebviewUri(vscode.Uri.joinPath(katexUri, 'katex.min.css'));
        const katexJsUri = webview.asWebviewUri(vscode.Uri.joinPath(katexUri, 'katex.min.js'));
        const katexAutoRenderUri = webview.asWebviewUri(vscode.Uri.joinPath(katexUri, 'contrib', 'auto-render.min.js'));

        // Use a strict CSP
        const nonce = getNonce();
        const csp = `default-src 'none'; font-src ${webview.cspSource}; style-src ${webview.cspSource} 'unsafe-inline'; script-src 'nonce-${nonce}';`;

        return `<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="Content-Security-Policy" content="${csp}">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Cadabra Inspector</title>

                <!-- KaTeX CSS -->
                <link rel="stylesheet" href="${katexCssUri}">
                
                <style>
                    body {
                        font-family: var(--vscode-font-family);
                        color: var(--vscode-editor-foreground);
                        background-color: var(--vscode-editor-background);
                        padding: 20px;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                    }
                    h2 {
                        color: var(--vscode-editorInfo-foreground);
                        margin-bottom: 20px;
                    }
                    .math-container {
                        font-size: 2em; /* Big math */
                        margin: 20px 0;
                        padding: 20px;
                        width: 100%;
                        overflow-x: auto; /* Horizontal scroll if too long */
                        text-align: center;
                        background: var(--vscode-editorWidget-background);
                        border: 1px solid var(--vscode-editorWidget-border);
                        border-radius: 6px;
                        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    }
                    .raw-latex {
                        width: 100%;
                        max-width: 800px;
                        margin-top: 30px;
                        padding: 15px;
                        background-color: var(--vscode-textCodeBlock-background);
                        border-left: 4px solid var(--vscode-editorInfo-foreground);
                        overflow-x: auto;
                        font-family: var(--vscode-editor-font-family);
                        font-size: 0.9em;
                        white-space: pre-wrap;
                        word-break: break-all;
                    }
                </style>
            </head>
            <body>
                <h2>Variable: <code>${name}</code></h2>

                <!-- Rendered Math -->
                <div class="math-container" id="math-element">
                    <!-- KaTeX will render here -->
                </div>

                <!-- Raw LaTeX (for debugging) -->
                <div class="raw-latex">
<strong>Raw LaTeX:</strong>
<br/><br/>
${escapeHtml(latex)}
                </div>

                <!-- KaTeX JS Scripts -->
                <script nonce="${nonce}" src="${katexJsUri}"></script>
                
                <script nonce="${nonce}">
                    // We must escape backslashes to correctly pass them from JS to KaTeX
                    const latexString = ${JSON.stringify(latex)};
                    
                    document.addEventListener("DOMContentLoaded", function() {
                        const mathElement = document.getElementById('math-element');
                        try {
                            katex.render(latexString, mathElement, {
                                throwOnError: false,
                                displayMode: true,
                                strict: false
                            });
                        } catch (err) {
                            mathElement.innerText = "Error rendering KaTeX: " + err.message;
                        }
                    });
                </script>
            </body>
            </html>`;
    }
}

function getNonce() {
    let text = '';
    const possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for (let i = 0; i < 32; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    }
    return text;
}

function escapeHtml(unsafe: string) {
    return unsafe
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
}
