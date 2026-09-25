import * as vscode from 'vscode';

export class CadabraPreviewProvider implements vscode.WebviewViewProvider {
    public static readonly viewType = 'cadabraPreviewView';

    private _view?: vscode.WebviewView;
    private readonly _extensionUri: vscode.Uri;
    private _currentName: string = '';
    private _currentLatex: string = '';
    private _currentInputForm: string = '';

    constructor(extensionUri: vscode.Uri) {
        this._extensionUri = extensionUri;
    }

    public resolveWebviewView(
        webviewView: vscode.WebviewView,
        context: vscode.WebviewViewResolveContext,
        _token: vscode.CancellationToken,
    ) {
        this._view = webviewView;

        webviewView.webview.options = {
            enableScripts: true,
            localResourceRoots: [vscode.Uri.joinPath(this._extensionUri, 'node_modules', 'katex', 'dist')]
        };

        webviewView.webview.onDidReceiveMessage(message => {
            if (message.command === 'copy') {
                vscode.env.clipboard.writeText(message.text).then(() => {
                    vscode.window.showInformationMessage('Raw LaTeX copiado al portapapeles');
                });
            }
        });

        this._updateWebview();
    }

    public updateContent(name: string, latex: string, inputForm: string) {
        this._currentName = name;
        this._currentLatex = latex;
        this._currentInputForm = inputForm;
        this._updateWebview();
    }

    private _sanitizeLatexForKatex(latex: string): string {
        // Prepend \displaystyle and replace \discretionary with \allowbreak
        // This creates a hybrid inline-display mode that wraps naturally.
        return "\\displaystyle " + latex.replace(/\\discretionary\{\}\{\}\{\}/g, '\\allowbreak ');
    }

    private _updateWebview() {
        if (!this._view) {
            return;
        }

        // Handle messages from the webview
        if (!this._view.webview.onDidReceiveMessage) {
            // Already handled, but let's ensure we only register once per view
        }
        
        // Actually, we should register the message listener in resolveWebviewView,
        // but since we only resolve once, we'll do it there.

        if (!this._currentName) {
            this._view.webview.html = this._getEmptyHtml();
            return;
        }

        this._view.webview.html = this._getHtmlForWebview(this._view.webview, this._currentName, this._currentLatex, this._currentInputForm);
    }

    private _getEmptyHtml(): string {
        return `<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <style>
                    body {
                        font-family: var(--vscode-font-family);
                        color: var(--vscode-descriptionForeground);
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        padding: 0;
                    }
                </style>
            </head>
            <body>
                <p>Select a variable to preview</p>
            </body>
            </html>`;
    }

    private _getHtmlForWebview(webview: vscode.Webview, name: string, latex: string, inputForm: string) {
        // Local path to KaTeX assets
        const katexUri = vscode.Uri.joinPath(this._extensionUri, 'node_modules', 'katex', 'dist');

        const katexCssUri = webview.asWebviewUri(vscode.Uri.joinPath(katexUri, 'katex.min.css'));
        const katexJsUri = webview.asWebviewUri(vscode.Uri.joinPath(katexUri, 'katex.min.js'));

        // Use a strict CSP
        const nonce = getNonce();
        const csp = `default-src 'none'; font-src ${webview.cspSource}; style-src ${webview.cspSource} 'unsafe-inline'; script-src 'nonce-${nonce}';`;

        // We need both the original RAW latex and the sanitized one for KaTeX
        const renderLatex = this._sanitizeLatexForKatex(latex);

        return `<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="Content-Security-Policy" content="${csp}">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Cadabra Preview</title>

                <!-- KaTeX CSS -->
                <link rel="stylesheet" href="${katexCssUri}">
                
                <style>
                    body {
                        font-family: var(--vscode-font-family);
                        color: var(--vscode-editor-foreground);
                        background-color: var(--vscode-editor-background);
                        padding: 10px;
                        margin: 0;
                        display: flex;
                        flex-direction: column;
                    }
                    .math-container {
                        font-size: 1.5em; /* Scaled slightly down for sidebar */
                        margin: 10px 0;
                        padding: 10px;
                        width: 100%;
                        text-align: center;
                        box-sizing: border-box;
                        /* Removed overflow-x to allow vertical wrapping */
                    }
                    .details-container {
                        margin-top: 20px;
                        border-top: 1px solid var(--vscode-panel-border);
                        padding-top: 10px;
                    }
                    summary {
                        cursor: pointer;
                        color: var(--vscode-editorInfo-foreground);
                        font-weight: bold;
                        user-select: none;
                        margin-bottom: 10px;
                    }
                    .raw-box {
                        background-color: var(--vscode-textCodeBlock-background);
                        padding: 10px;
                        border-radius: 4px;
                        font-family: var(--vscode-editor-font-family);
                        font-size: 0.9em;
                        white-space: pre-wrap;
                        word-break: break-all;
                        max-height: 200px;
                        overflow-y: auto;
                        margin-bottom: 10px;
                    }
                    .copy-btn {
                        background-color: var(--vscode-button-background);
                        color: var(--vscode-button-foreground);
                        border: none;
                        padding: 6px 12px;
                        cursor: pointer;
                        border-radius: 2px;
                        font-family: var(--vscode-font-family);
                        width: 100%;
                    }
                    .copy-btn:hover {
                        background-color: var(--vscode-button-hoverBackground);
                    }
                </style>
            </head>
            <body>
                <!-- Rendered Math -->
                <div class="math-container" id="math-element">
                    <!-- KaTeX will render here -->
                </div>
                
                <div class="details-container">
                    <details>
                        <summary>Raw Expression ▾</summary>
                        <div class="raw-box">${escapeHtml(inputForm)}</div>
                    </details>
                    <button class="copy-btn" id="copy-btn">📋 Copiar</button>
                </div>

                <!-- KaTeX JS Scripts -->
                <script nonce="${nonce}" src="${katexJsUri}"></script>
                
                <script nonce="${nonce}">
                    const vscode = acquireVsCodeApi();
                    
                    // The transformed LaTeX for KaTeX
                    const renderLatexStr = ${JSON.stringify(renderLatex)};
                    
                    // The untouched original RAW expression for copying
                    const inputFormStr = ${JSON.stringify(inputForm)};
                    
                    document.addEventListener("DOMContentLoaded", function() {
                        const mathElement = document.getElementById('math-element');
                        try {
                            katex.render(renderLatexStr, mathElement, {
                                throwOnError: false,
                                displayMode: false, // Must be false for \\allowbreak to wrap!
                                strict: false
                            });
                        } catch (err) {
                            mathElement.innerText = "Error rendering KaTeX: " + err.message;
                        }
                        
                        document.getElementById('copy-btn').addEventListener('click', () => {
                            vscode.postMessage({
                                command: 'copy',
                                text: inputFormStr
                            });
                        });
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
