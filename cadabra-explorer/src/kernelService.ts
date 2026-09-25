import * as vscode from 'vscode';
import { exec } from 'child_process';
import * as fs from 'fs';

export interface CadabraVariable {
    name: string;
    type: string;
    preview: string;
    latex: string;
    inputForm: string;
}

export class KernelService {
    private readonly scriptPath: string;

    constructor(extensionUri: vscode.Uri) {
        this.scriptPath = vscode.Uri.joinPath(extensionUri, 'src', 'scripts', 'query_kernel_safe.py').fsPath;
    }

    public async getVariables(notebookUri: vscode.Uri | undefined): Promise<CadabraVariable[]> {
        if (!notebookUri) {
            throw new Error("No active notebook found.");
        }

        const connectionFile = this.getConnectionFile();
        if (!connectionFile) {
            throw new Error("Kernel disconnected / Run a cell to connect");
        }

        const payload = { action: "list" };
        const payloadString = JSON.stringify(payload);
        const command = `python3 ${this.scriptPath} ${connectionFile} '${payloadString}'`;

        return new Promise((resolve, reject) => {
            exec(command, (error, stdout, stderr) => {
                if (error) {
                    reject(new Error(`Kernel error: ${error.message}`));
                    return;
                }

                try {
                    const jsonResponse = JSON.parse(stdout);
                    if (jsonResponse.error) {
                        reject(new Error(jsonResponse.error));
                        return;
                    }
                    resolve(jsonResponse as CadabraVariable[]);
                } catch (e: any) {
                    reject(new Error(`JSON Parsing Error: ${e.message}. STDOUT: ${stdout}`));
                }
            });
        });
    }

    private getConnectionFile(): string | null {
        // Fallback OS Heuristic
        const runtimeDir = "/run/user/1000/jupyter/runtime/";
        if (fs.existsSync(runtimeDir)) {
            const files = fs.readdirSync(runtimeDir)
                .filter(f => f.startsWith('kernel-') && f.endsWith('.json'))
                .map(f => ({
                    name: f,
                    time: fs.statSync(runtimeDir + f).mtime.getTime()
                }))
                .sort((a, b) => b.time - a.time);
                
            if (files.length > 0) {
                return runtimeDir + files[0].name;
            }
        }
        return null;
    }
}
