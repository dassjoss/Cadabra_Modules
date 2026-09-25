import * as vscode from 'vscode';
import { KernelService, CadabraVariable } from './kernelService';

export class CadabraVariableProvider implements vscode.TreeDataProvider<vscode.TreeItem> {
    private _onDidChangeTreeData: vscode.EventEmitter<vscode.TreeItem | undefined | null | void> = new vscode.EventEmitter<vscode.TreeItem | undefined | null | void>();
    readonly onDidChangeTreeData: vscode.Event<vscode.TreeItem | undefined | null | void> = this._onDidChangeTreeData.event;

    private kernelService: KernelService;
    private notebookUri: vscode.Uri | undefined;

    constructor(kernelService: KernelService) {
        this.kernelService = kernelService;
    }

    public refresh(notebookUri: vscode.Uri | undefined): void {
        this.notebookUri = notebookUri;
        this._onDidChangeTreeData.fire();
    }

    getTreeItem(element: vscode.TreeItem): vscode.TreeItem {
        return element;
    }

    async getChildren(element?: vscode.TreeItem): Promise<vscode.TreeItem[]> {
        if (element) {
            return []; // No nested items yet
        }

        if (!this.notebookUri) {
            return [this.createMessageItem("No active notebook found", "$(warning)")];
        }

        try {
            const variables = await this.kernelService.getVariables(this.notebookUri);
            
            if (variables.length === 0) {
                return [this.createMessageItem("No Cadabra variables found", "$(info)")];
            }

            return variables.map(v => {
                const item = new vscode.TreeItem(v.name, vscode.TreeItemCollapsibleState.None);
                item.description = v.preview.length > 50 ? v.preview.substring(0, 47) + "..." : v.preview;
                
                // Construct Markdown tooltip with math block
                const tooltip = new vscode.MarkdownString();
                tooltip.appendMarkdown(`**${v.name}** (${v.type})\n\n`);
                // Use $$ for display math rendering in VS Code Markdown
                tooltip.appendMarkdown(`$$\n${v.latex}\n$$\n\n`);
                tooltip.appendMarkdown(`---\n*Raw LaTeX:*\n\`\`\`latex\n${v.latex}\n\`\`\``);
                tooltip.supportHtml = true;
                
                item.tooltip = tooltip;
                item.iconPath = new vscode.ThemeIcon("symbol-variable");
                
                // Command for selection/inspection
                item.command = {
                    command: 'cadabraExplorer.inspectVariable',
                    title: 'Inspect Variable',
                    arguments: [v.name, v.latex, v.inputForm]
                };
                return item;
            });

        } catch (error: any) {
            if (error.message.includes("Kernel disconnected") || error.message.includes("Valid connection file not found")) {
                return [this.createMessageItem("Kernel disconnected (Run a cell to connect)", "$(plug)")];
            }
            return [this.createMessageItem(`Error: ${error.message}`, "$(error)")];
        }
    }

    private createMessageItem(message: string, iconId: string): vscode.TreeItem {
        const item = new vscode.TreeItem(message, vscode.TreeItemCollapsibleState.None);
        item.iconPath = new vscode.ThemeIcon(iconId.replace('$(', '').replace(')', ''));
        return item;
    }
}
