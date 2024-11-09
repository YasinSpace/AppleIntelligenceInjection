import asyncio
import subprocess

async def ask_ai(input_text):
    formatted_input = f"system A conversation between a user and a helpful understanding assistant. Always answer the user queries and questions. Continue this conversation. {input_text}"
    
    apple_script_command = f"""
    set a to path to frontmost application as text

    tell application "Notes"
        set folderExists to false
        tell account "iCloud"
            repeat with f in folders
                if name of f is "Apple Intelligence" then
                    set folderExists to true
                    exit repeat
                end if
            end repeat
            
            if folderExists is false then
                make new folder with properties {{name:"Apple Intelligence"}}
            end if
            
            set newNote to make new note at folder "Apple Intelligence" with properties {{name:"Apple Intelligence Chatbot", body:"{formatted_input}"}}
            delay 0.2
            show newNote
            delay 0.2
        end tell
    end tell

    tell application "System Events"
        key code 124
        delay 0.1
        keystroke "a" using {{command down}}
        delay 0.1
        key code 126
        delay 0.1
        key code 125
        delay 0.1
        key code 125 using {{command down, shift down}}
    end tell

    set startTime to current date
    tell application "System Events"
        keystroke "c" using command down
    end tell
    delay 0.1
    set initialClipboard to the clipboard

    tell application "System Events"
        delay 0.1
        tell application "Notes" to activate
        tell process "Notes"
            click menu bar item "Edit" of menu bar 1

            click menu item "Writing Tools" of menu "Edit" of menu bar item "Edit" of menu bar 1
            delay 0.1

            click menu item "Rewrite" of menu 1 of menu item "Writing Tools" of menu "Edit" of menu bar item "Edit" of menu bar 1
            delay 0.1
        end tell
    end tell

    repeat
        delay 1
        
        tell application "System Events"
            keystroke "c" using command down
        end tell
        
        set currentClipboard to the clipboard
        
        if currentClipboard is not initialClipboard then
            delay 0.5
            tell application "Notes"
                delete newNote
            end tell
            delay 0.5
            activate application a
            delay 0.1
            return currentClipboard
        end if
    end repeat
    """
    
    process = await asyncio.create_subprocess_shell(
        f"osascript -e '{apple_script_command}'",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    stdout, stderr = await process.communicate()
    if process.returncode != 0:
        raise Exception(f"Error executing osascript: {stderr.decode().strip()}")
    
    return stdout.decode().strip()

async def main():
    convo = ""
    while True:
        try:
            user_input = input("Apple Intelligence > ")
            convo += f" [user]: {user_input.strip()} [assistant]: "
            response = await ask_ai(convo)
            
            if "«class utf8»:" in response:
                utf8_index = response.find("«class utf8»:")
                if utf8_index != -1:
                    response = response[utf8_index + len("«class utf8»:"):].strip()
            
            convo += f"{response}"
            print(response)
        
        except Exception as error:
            print(f"Error: {error}")
        except KeyboardInterrupt:
            print("^C")
            break

# Run the async main function
asyncio.run(main())
