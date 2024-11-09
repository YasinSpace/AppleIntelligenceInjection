# AppleIntelligenceInjection

![1](https://github.com/user-attachments/assets/ca421fce-1225-4390-9c26-0c332a60cdd3)

This script is a Python-based application that uses a prompt injection technique to interact with a virtual assistant within the macOS Notes app. By leveraging AppleScript and macOS’s automation capabilities, the script creates an integrated chatbot experience directly within Notes, capable of responding to user queries.
# Key Components and Workflow
## Prompt Injection Setup
- [x] The script takes user input as a prompt and formats it with additional context to create an injected command, guiding the assistant’s response style and content.
- [x] Each user query is appended to an ongoing conversation format, preserving the context of previous interactions.
## AppleScript Automation
- [x] The main functionality is executed via AppleScript, which is embedded in the Python script. This AppleScript does several things:
- [x] Checks if a folder named “Apple Intelligence” exists within iCloud in the Notes app. If it doesn’t, it creates one.
- [x] Creates a new note with the injected prompt as its content, effectively “asking” the virtual assistant to respond based on the context and previous prompts.
- [x] Displays this note to the user and moves the focus to it.
- [x] After the prompt injection, AppleScript uses System Events to simulate keyboard actions. This includes navigating menus and using key combinations to activate the assistant’s response or text rewriting tools within the Notes app.
## Clipboard Monitoring for Response Capture
- [x] Once the assistant has generated a response in the Note, the script copies the content to the clipboard by simulating the “Command + C” keyboard shortcut.
- [x] The script continuously checks the clipboard for changes, detecting when a response has been generated. This approach ensures that the response is captured and retrieved without manual intervention.
- [x] When the clipboard changes, the response is stored and returned to the user, and the temporary note is deleted from Notes.
## Error Handling
- [x] The script includes basic error handling, catching issues related to AppleScript execution (such as permission errors or missing folders) and notifying the user.
## 5. Prompt Injection as the Core Feature:
- [x] Prompt injection is the key technique here, where user input is combined with guiding context to influence the assistant’s behavior. This technique allows for conversational continuity and ensures that the assistant’s responses are controlled and aligned with the user’s intent.

![2](https://github.com/user-attachments/assets/3db2e1f1-d002-4318-9124-3e70764019bc)

# Example Use Case

This script is ideal for users who want to experiment with prompt engineering and chatbot responses in a unique, macOS-integrated way. For instance:
- [x] A user can ask a question like, “What’s the weather today?” and have the assistant provide a response.
- [x] The assistant can then maintain context as the user asks follow-up questions, resulting in a cohesive conversational experience entirely within the Notes app.

# Requirements and Permissions

For this script to work properly, the following permissions and requirements must be met:
- [x] Accessibility Access: The terminal app (e.g., Terminal or iTerm) running the script needs accessibility permissions to control the Notes app and simulate keyboard actions.
- [x] Automation Permissions: The script needs permission to control applications like System Events and Notes.
- [x] iCloud Access: The Notes folder should be created under an iCloud account in the Notes app to ensure accessibility across devices.

# Potential Use Cases and Limitations

This approach provides a flexible environment for experimenting with prompt injections but has some limitations:
- [x] Platform Restriction: Only works on macOS due to the reliance on AppleScript and System Events.
- [x] Privacy and Security: macOS may prompt for additional permissions as the script accesses Notes and clipboard contents, which could raise privacy concerns in secure environments.
