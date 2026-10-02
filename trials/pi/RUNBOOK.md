# Pi Coding Agent Framework — Learning Runbook

Last updated: 2026-09-06

## Mission

**Why:** Build and customize a coding agent using pi's minimal framework — understand the agent loop, tool system, and extensibility model well enough to adapt pi to my own workflows rather than conforming to opinionated product constraints.

**Success looks like:**
- Install pi and run a basic coding agent session against a real repository task
- Understand the agent loop: how pi processes prompts, calls tools, and decides when it's done
- Add a custom tool or skill and see the agent use it
- Configure pi to use my preferred LLM provider (Claude, GPT-4, or another)
- Extend pi with a TypeScript Extension for a custom workflow

**Constraints:** 4–6 hours across 4 days (~60–90 min/day); npm and Node.js installed; a test repository for the agent to work on; access to at least one LLM API key (Claude or OpenAI).

**Out of scope:** TUI customization, Slack bot integration, building a full application on pi's SDK, vLLM pod deployment, contributing upstream features, security hardening for production use.

## Why Pi?

Pi positions itself as a **minimal, self-extensible** coding agent framework:
- **Terminal-first**: Lives in your terminal, not a GUI product
- **Provider-agnostic**: Works with 20+ LLM providers (Claude, GPT-4, Gemini, DeepSeek, Grok, etc.)
- **Modular architecture**: Layered packages let you use what you need (LLM client, agent loop, full coding agent, TUI)
- **Extensible**: TypeScript Extensions, Skills, Prompt Templates, and Themes
- **Open source** (MIT): No product lock-in, full transparency

Pi became notable as the engine behind [OpenClaw](https://gist.github.com/dabit3/e97dbfe71298b1df4d36542aceb5f158), which reached 145,000+ GitHub stars. It's a response to limitations in existing coding agent products — maximum control with minimal opinion.

## Prerequisites

Before starting:
- Node.js 18+ and npm installed (`node --version`, `npm --version`)
- At least one LLM API key set up (Claude via `ANTHROPIC_API_KEY`, OpenAI via `OPENAI_API_KEY`, etc.)
- A small test repository to practice on (or create one during the session)
- Basic TypeScript/JavaScript familiarity for extensions (can learn as you go)

## Learning Path

### Session 1: Installation and First Agent Run (~60 min)

**Objective:** Install pi, configure an LLM provider, and successfully run your first coding agent session on a simple task.

**Steps:**

1. **Install pi globally**
   ```bash
   npm install -g @mariozechner/pi-coding-agent
   ```
   Verify: `pi --version` should print the installed version.

2. **Set up your LLM provider**
   
   For Claude (recommended if you have Anthropic API access):
   ```bash
   export ANTHROPIC_API_KEY="your-api-key-here"
   ```
   
   For OpenAI:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```
   
   Add to your shell profile (`~/.zshrc` or `~/.bashrc`) to persist across sessions.

3. **Create or navigate to a test repository**
   ```bash
   mkdir -p ~/test-repos/pi-practice
   cd ~/test-repos/pi-practice
   git init
   echo "# Pi Practice Repo" > README.md
   git add README.md
   git commit -m "Initial commit"
   ```

4. **Start your first pi session**
   ```bash
   pi
   ```
   
   Pi will prompt you to select an LLM provider if multiple are available. Choose one.
   
5. **Give the agent a simple task**
   
   At the pi prompt, try:
   ```
   Create a simple Node.js script called hello.js that prints "Hello from Pi!" to the console.
   ```
   
   Observe:
   - How pi analyzes the task
   - What tools it calls (file creation, reading, etc.)
   - When it considers the task complete
   - The session persistence (pi saves the conversation)

6. **Verify the result**
   ```bash
   node hello.js
   ```
   Should print: `Hello from Pi!`

7. **Exit and resume**
   - Type `exit` or press Ctrl+D to end the session
   - Run `pi` again — notice pi can resume from the saved session or start fresh

**Check yourself:**
- [ ] Pi installed and runs without errors
- [ ] Successfully completed a simple file-creation task
- [ ] Observed the agent loop in action (prompt → tool calls → completion)
- [ ] Session persistence working (can resume or start fresh)

**What you learned:**
- Pi runs as a CLI tool, not a GUI app
- The agent loop: analyze task → plan → call tools → verify → report
- Sessions are saved automatically (find them in pi's data directory)
- Pi can work with files in your current directory

---

### Session 2: Understanding the Agent Loop and Tool System (~75 min)

**Objective:** Understand how pi's agent loop works, what built-in tools it has, and when the agent decides a task is done.

**Steps:**

1. **Read pi's help and available commands**
   ```bash
   pi --help
   ```
   Note the flags: `--model`, `--provider`, `--verbose`, `--debug`, `--new-session`

2. **Start a verbose session to see tool calls**
   ```bash
   pi --verbose
   ```
   
3. **Give a multi-step task that requires tool orchestration**
   ```
   Create a simple Express.js server in server.js:
   - Install express if needed (package.json + npm install)
   - Set up a GET / endpoint that returns "Hello World"
   - Add a GET /api/status endpoint that returns JSON: { status: "ok", timestamp: <current time> }
   - Make sure it runs on port 3000
   ```

4. **Observe the agent loop**
   
   Watch for:
   - **Planning phase**: How does pi break down the task?
   - **Tool calls**: What tools does pi use? (file write, shell commands, file read for verification)
   - **Verification**: Does pi test that the server code is correct?
   - **Completion**: When does pi say "done"? What signals completion?

5. **Explore built-in tools**
   
   Check the [pi SDK docs](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sdk.md) or pi's code to understand available tools:
   - File operations: read, write, edit, delete, list directory
   - Shell commands: execute bash/shell commands
   - Git operations (if supported)
   - Code analysis tools (grep, find, etc.)

6. **Test the agent's error handling**
   
   Give an intentionally broken task:
   ```
   Create a Python script that imports a nonexistent module and prints a message.
   ```
   
   Observe:
   - Does pi catch the error when trying to run it?
   - Does it attempt to fix the issue?
   - What does the agent do when it can't complete the task?

7. **Check session history**
   
   Find where pi stores session data (usually `~/.pi/` or similar). Look at:
   - Conversation history (JSON or markdown)
   - Tool call logs
   - Session metadata

**Check yourself:**
- [ ] Can identify the phases of pi's agent loop (plan → execute → verify → report)
- [ ] Know what built-in tools pi has and when it uses each
- [ ] Understand when pi considers a task "complete"
- [ ] Can find and read session history files
- [ ] Observed how pi handles errors and incomplete information

**What you learned:**
- Pi's agent loop: iterative refinement until task completion or stuck state
- Built-in tools cover common coding tasks (files, shell, git)
- Pi saves full session state (conversation + tool calls)
- Verbose/debug flags reveal the agent's decision-making

---

### Session 3: Configuration and Provider Switching (~60 min)

**Objective:** Configure pi to use different LLM providers, understand model selection trade-offs, and set up persistent configuration.

**Steps:**

1. **Check current configuration**
   ```bash
   pi config show
   # or check ~/.pi/config.json if it exists
   ```

2. **Try different LLM providers**
   
   If you have multiple API keys set up:
   
   **Switch to GPT-4:**
   ```bash
   export OPENAI_API_KEY="your-key"
   pi --provider openai --model gpt-4-turbo
   ```
   
   **Switch to Claude:**
   ```bash
   export ANTHROPIC_API_KEY="your-key"
   pi --provider anthropic --model [REDACTED]
   ```
   
   **Try Gemini (if available):**
   ```bash
   export GOOGLE_API_KEY="your-key"
   pi --provider google --model gemini-2.0-flash-exp
   ```

3. **Compare behavior across models**
   
   Give the same task to different models:
   ```
   Refactor this hello.js file to use ES6 imports and add JSDoc comments.
   ```
   
   Observe:
   - Speed differences
   - Tool call patterns
   - Code quality
   - Cost (check API usage logs)

4. **Set a default provider and model**
   
   Create or edit `~/.pi/config.json`:
   ```json
   {
     "defaultProvider": "anthropic",
     "defaultModel": "[REDACTED]",
     "verbose": false,
     "saveHistory": true
   }
   ```

5. **Understand model trade-offs**
   
   | Model | Speed | Quality | Cost | Best for |
   |-------|-------|---------|------|----------|
   | Claude Sonnet 5 | Fast | High | Medium | General coding, complex tasks |
   | GPT-4 Turbo | Medium | High | High | Deep reasoning, architecture |
   | Gemini Flash | Very Fast | Medium | Low | Quick edits, simple tasks |
   | DeepSeek Coder | Fast | Medium-High | Low | Code-specific tasks |

6. **Test with a local/self-hosted model (optional)**
   
   If you have Ollama or another local LLM:
   ```bash
   pi --provider ollama --model codellama
   ```

**Check yourself:**
- [ ] Successfully switched between at least 2 different LLM providers
- [ ] Created a persistent config file with your preferred defaults
- [ ] Observed behavioral differences between models
- [ ] Understand the speed/quality/cost trade-offs

**What you learned:**
- Pi is truly provider-agnostic — swap models without changing your workflow
- Different models have different strengths (speed vs. quality vs. cost)
- Configuration can be set per-session (flags) or persistent (config file)
- Local models are an option for cost/privacy concerns

---

### Session 4: Adding Custom Tools and Extensions (~90 min)

**Objective:** Extend pi with a custom tool or TypeScript Extension, then watch the agent use it in a real task.

**Steps:**

1. **Understand pi's extension system**
   
   Read the [pi SDK documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sdk.md) to understand:
   - **Skills**: Reusable prompt templates
   - **Tools**: Custom functions the agent can call
   - **Extensions**: TypeScript modules that add new capabilities
   - **Themes**: UI/TUI customization

2. **Create your first custom tool**
   
   Create `~/.pi/extensions/custom-tools.ts`:
   ```typescript
   import { Tool } from '@mariozechner/pi-agent-core';
   
   export const timestampTool: Tool = {
     name: 'get_timestamp',
     description: 'Get the current timestamp in ISO format',
     parameters: {
       type: 'object',
       properties: {
         format: {
           type: 'string',
           enum: ['iso', 'unix', 'human'],
           description: 'The format for the timestamp'
         }
       },
       required: ['format']
     },
     handler: async (params) => {
       const now = new Date();
       switch (params.format) {
         case 'iso':
           return now.toISOString();
         case 'unix':
           return Math.floor(now.getTime() / 1000).toString();
         case 'human':
           return now.toLocaleString();
         default:
           return now.toISOString();
       }
     }
   };
   ```

3. **Register the custom tool**
   
   Update your pi config to load the extension:
   ```json
   {
     "extensions": ["~/.pi/extensions/custom-tools.ts"],
     "defaultProvider": "anthropic",
     "defaultModel": "[REDACTED]"
   }
   ```

4. **Test the custom tool**
   
   Start pi and give a task that would benefit from your tool:
   ```
   Create a log.txt file with an entry that includes the current timestamp in ISO format.
   ```
   
   Observe:
   - Does pi discover and call your `get_timestamp` tool?
   - How does it decide to use your tool vs. built-in alternatives?

5. **Create a more complex extension: repo context tool**
   
   Create `~/.pi/extensions/repo-context.ts`:
   ```typescript
   import { Tool } from '@mariozechner/pi-agent-core';
   import { execSync } from 'child_process';
   
   export const repoContextTool: Tool = {
     name: 'get_repo_context',
     description: 'Get high-level context about the current git repository (languages, structure, recent commits)',
     parameters: {
       type: 'object',
       properties: {
         depth: {
           type: 'number',
           description: 'How many recent commits to include (default 5)',
           default: 5
         }
       }
     },
     handler: async (params) => {
       try {
         const depth = params.depth || 5;
         
         // Get language breakdown
         const languages = execSync('git ls-files | xargs file | grep -E "text|script" | cut -d: -f2 | sort | uniq -c | sort -rn', 
           { encoding: 'utf-8', stdio: 'pipe' }).trim();
         
         // Get recent commits
         const commits = execSync(`git log --oneline -${depth}`, 
           { encoding: 'utf-8', stdio: 'pipe' }).trim();
         
         // Get directory structure
         const tree = execSync('tree -L 2 -I "node_modules|.git" || find . -maxdepth 2 -type d', 
           { encoding: 'utf-8', stdio: 'pipe' }).trim();
         
         return JSON.stringify({
           languages,
           recentCommits: commits.split('\n'),
           structure: tree.split('\n')
         }, null, 2);
       } catch (error) {
         return `Error getting repo context: ${error.message}`;
       }
     }
   };
   ```

6. **Test the repo context tool**
   
   Give pi a task that requires understanding the repo:
   ```
   Look at this repository's context and suggest what kind of documentation would be most useful to add.
   ```

7. **Create a custom skill (prompt template)**
   
   Create `~/.pi/skills/code-review.md`:
   ```markdown
   # Code Review Skill
   
   When reviewing code:
   1. Check for common issues: unused variables, missing error handling, security concerns
   2. Assess readability: naming, comments, structure
   3. Suggest improvements with specific examples
   4. Highlight what's done well
   
   Output format:
   - Issues Found: [list]
   - Suggestions: [list]
   - Positive Observations: [list]
   ```
   
   Tell pi:
   ```
   Use the code-review skill to review the server.js file we created earlier.
   ```

**Check yourself:**
- [ ] Created and registered at least one custom tool
- [ ] Observed the agent successfully calling your custom tool
- [ ] Understand how tools are described to the LLM (name, description, parameters)
- [ ] Created a custom skill (prompt template)
- [ ] Know where to find the extension/skill documentation

**What you learned:**
- Pi's tool system uses standard function-calling interfaces
- Custom tools expand what the agent can do beyond built-in capabilities
- Skills are reusable prompt patterns (lightweight extensions)
- Extensions are full TypeScript modules with access to pi's internals
- The LLM decides when to use your tool based on its description

---

## After the Learning Path

### Next steps:
1. **Build a custom workflow**: Use pi's SDK to embed the agent in your own script or tool
2. **Explore the TUI**: Try `pi-tui` for a richer terminal interface
3. **Multi-agent patterns**: Use pi to coordinate multiple agents on complex tasks
4. **Contribute upstream**: Submit your custom tools/skills as PRs to the pi repo
5. **Production hardening**: Add error handling, rate limiting, cost controls for real use

### Resources:
- [Pi GitHub repo](https://github.com/earendil-works/pi)
- [Pi SDK documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sdk.md)
- [How to Build a Custom Agent Framework with PI](https://gist.github.com/dabit3/e97dbfe71298b1df4d36542aceb5f158)
- [Agent Pi: Anatomy of a Minimal Coding Agent](https://shivamagarwal7.medium.com/agentic-ai-pi-anatomy-of-a-minimal-coding-agent-powering-openclaw-5ecd4dd6b440)
- [Building Pi: A Minimal, Extensible Coding Agent Framework](https://www.zenml.io/llmops-database/building-pi-a-minimal-extensible-coding-agent-framework)

### Common pitfalls:
- **Tool description matters**: If the LLM doesn't call your tool, revise the description to be clearer about when to use it
- **Error handling**: Custom tools need robust error handling or they'll crash the agent
- **Cost tracking**: Pi doesn't have built-in cost monitoring — track API usage yourself
- **Session management**: Long sessions can get expensive/slow — know when to start fresh
- **Local vs. remote models**: Local models are cheaper but often lower quality — test your workflow with both

---

## Session Log Template

Copy this template for each session:

```markdown
### Session N: [Topic] — [Date]

**Time spent:** [actual minutes]

**What I tried:**
- 

**What worked:**
- 

**What didn't:**
- 

**Key insight:**
- 

**Questions for next session:**
- 

**Tool/extension built:**
- 
```

---

## Completion Criteria

You've completed this learning path when you can:
- [ ] Install and configure pi with your preferred LLM provider
- [ ] Run the agent on a real coding task and understand each phase of the agent loop
- [ ] Switch between LLM providers and understand trade-offs
- [ ] Create a custom tool and watch the agent use it
- [ ] Explain how pi differs from Claude Code, Cursor, or other coding assistants
- [ ] Decide whether pi's minimal approach fits your workflow better than opinionated products

**Final test:** Build a custom tool that solves a problem in YOUR actual workflow (not a toy example), register it with pi, and successfully complete a real task using it.

---

**Sources:**
- [Pi GitHub Repository](https://github.com/earendil-works/pi)
- [Pi SDK Documentation](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/sdk.md)
- [How to Build a Custom Agent Framework with PI](https://gist.github.com/dabit3/e97dbfe71298b1df4d36542aceb5f158)
- [Agent Pi: Anatomy of a Minimal Coding Agent](https://shivamagarwal7.medium.com/agentic-ai-pi-anatomy-of-a-minimal-coding-agent-powering-openclaw-5ecd4dd6b440)
- [Building Pi: Minimal, Extensible Coding Agent Framework](https://www.zenml.io/llmops-database/building-pi-a-minimal-extensible-coding-agent-framework)
- [Pi Website](https://pi.dev/)
