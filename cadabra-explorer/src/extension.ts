import * as vscode from 'vscode';
import { KernelService } from './kernelService';
import { CadabraVariableProvider } from './variableProvider';
import { CadabraPreviewProvider } from './previewWebview';

export function activate(context: vscode.ExtensionContext) {
    const kernelService = new KernelService(context.extensionUri);
    const variableProvider = new CadabraVariableProvider(kernelService);

    // Register TreeDataProvider
    vscode.window.registerTreeDataProvider('cadabraExplorerView', variableProvider);

    // Command: Manual Refresh
    let refreshCmd = vscode.commands.registerCommand('cadabraExplorer.refresh', () => {
        const activeEditor = vscode.window.activeNotebookEditor;
        variableProvider.refresh(activeEditor?.notebook.uri);
    });

    // Register WebviewViewProvider for the preview panel
    const previewProvider = new CadabraPreviewProvider(context.extensionUri);
    context.subscriptions.push(
        vscode.window.registerWebviewViewProvider(CadabraPreviewProvider.viewType, previewProvider)
    );

    // Command: Inspect Variable (Updates Preview)
    let inspectCmd = vscode.commands.registerCommand('cadabraExplorer.inspectVariable', (variableName: string, latex: string, inputForm: string) => {
        previewProvider.updateContent(variableName, latex, inputForm);
    });

    context.subscriptions.push(refreshCmd, inspectCmd);

    // Auto-refresh when active notebook changes
    vscode.window.onDidChangeActiveNotebookEditor(editor => {
        variableProvider.refresh(editor?.notebook.uri);
    });

    // Auto-refresh when a cell finishes execution
    vscode.workspace.onDidChangeNotebookDocument(e => {
        const activeEditor = vscode.window.activeNotebookEditor;
        if (activeEditor && e.notebook.uri.toString() === activeEditor.notebook.uri.toString()) {
            // Check if any cell execution finished
            const executionChanged = e.cellChanges.some(change => 
                change.executionSummary !== undefined || change.outputs !== undefined
            );
            if (executionChanged) {
                // Introduce a tiny delay to ensure the kernel is idle
                setTimeout(() => {
                    variableProvider.refresh(activeEditor.notebook.uri);
                }, 500);
            }
        }
    });

    // Initial load
    const activeEditor = vscode.window.activeNotebookEditor;
    variableProvider.refresh(activeEditor?.notebook.uri);
}

export function deactivate() {}
