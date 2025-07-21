import os
import tkinter as tk
from tkinter import messagebox
import webbrowser

file = r'%LOCALAPPDATA%\GitHubDesktop'
file = os.path.expandvars(file)

# auto-updating github desktop without user consent is annoying when there is a bug 
def toggle_update():
    global toggle_btn
    try:
        # Check if updates are currently enabled (Update.exe exists)
        update_file = os.path.join(file, 'Update.exe')
        annoying_file = os.path.join(file, 'AnnoyingUpdate.exe')
        
        if os.path.exists(update_file):
            # Disable updates
            print('Disabling updates...')
            new_file = os.path.join(file, 'AnnoyingUpdate.exe')
            os.rename(update_file, new_file)
            print('Successfully disabled updates')
            messagebox.showinfo("Success", "GitHub Desktop auto-updates disabled!")
            
            # Update button to show enable option
            toggle_btn.config(text="Enable Auto-Update", bg="#28a745", activebackground="#218838")
            
        elif os.path.exists(annoying_file):
            # Enable updates
            print('Enabling updates...')
            new_file = os.path.join(file, 'Update.exe')
            os.rename(annoying_file, new_file)
            print('Successfully enabled updates')
            messagebox.showinfo("Success", "GitHub Desktop auto-updates enabled!")
            
            # Update button to show disable option
            toggle_btn.config(text="Disable Auto-Update", bg="#dc3545", activebackground="#c82333")
            
        else:
            messagebox.showwarning("Warning", "Neither Update.exe nor AnnoyingUpdate.exe found.")
            
    except Exception as e:
        messagebox.showerror("Error", f"Failed to toggle updates: {str(e)}")

def open_github_issue():
    webbrowser.open("https://github.com/desktop/desktop/issues/3410")

def create_gui():
    root = tk.Tk()
    root.title("GitHub Desktop Annoying Update Fixer")
    root.geometry("500x500")
    root.resizable(False, False)
    
    # Dark mode styling
    root.configure(bg='#2d2d2d')
    
    # Center the window
    root.eval('tk::PlaceWindow . center')
    
    # Main frame
    main_frame = tk.Frame(root, padx=20, pady=20, bg='#2d2d2d')
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Title
    title_label = tk.Label(main_frame, text="GitHub Desktop Annoying Update Fixer", 
                          font=("Arial", 16, "bold"), bg='#2d2d2d', fg='#ffffff')
    title_label.pack(pady=(0, 20))
    
    # Description
    desc_text = """This tool helps you disable GitHub Desktop's annoying auto-updates.

The auto-updater can:
• Introduce new bugs
• Update without your consent
• Much more


Please support the official GitHub issue to add an opt-out setting!"""
    
    desc_label = tk.Label(main_frame, text=desc_text, 
                         font=("Arial", 10), justify=tk.LEFT, wraplength=450,
                         bg='#2d2d2d', fg='#e0e0e0')
    desc_label.pack(pady=(0, 20))
    
    # GitHub issue section
    issue_frame = tk.Frame(main_frame, bg='#2d2d2d')
    issue_frame.pack(fill=tk.X, pady=(0, 20))
    
    issue_label = tk.Label(issue_frame, text="Support the official GitHub issue:", 
                          font=("Arial", 11, "bold"), bg='#2d2d2d', fg='#ffffff')
    issue_label.pack()
    
    issue_link = tk.Label(issue_frame, text="https://github.com/desktop/desktop/issues/3410", 
                         fg="#4a9eff", cursor="hand2", font=("Arial", 9), bg='#2d2d2d')
    issue_link.pack(pady=(5, 10))
    issue_link.bind("<Button-1>", lambda e: open_github_issue())
    
    thumbs_up_btn = tk.Button(issue_frame, text="👍 Give a Thumbs Up!", 
                             command=open_github_issue, 
                             bg="#28a745", fg="white", font=("Arial", 11, "bold"),
                             relief=tk.RAISED, bd=2, activebackground="#1e7e34", activeforeground="white")
    thumbs_up_btn.pack(pady=(0, 10))
    
    # Action button
    button_frame = tk.Frame(main_frame, bg='#2d2d2d')
    button_frame.pack(fill=tk.X, pady=(20, 0))
    
    global toggle_btn
    
    # Check current state to set initial button appearance
    update_file = os.path.join(file, 'Update.exe')
    annoying_file = os.path.join(file, 'AnnoyingUpdate.exe')
    
    if os.path.exists(update_file):
        # Updates are enabled, show disable button
        button_text = "Disable Auto-Update"
        button_bg = "#dc3545"
        button_active_bg = "#c82333"
    elif os.path.exists(annoying_file):
        # Updates are disabled, show enable button
        button_text = "Enable Auto-Update"
        button_bg = "#28a745"
        button_active_bg = "#218838"
    else:
        raise Exception("Neither Update.exe nor AnnoyingUpdate.exe found.")
    
    toggle_btn = tk.Button(button_frame, text=button_text, 
                          command=toggle_update, 
                          bg=button_bg, fg="white", font=("Arial", 12, "bold"),
                          relief=tk.RAISED, bd=3, padx=20, pady=10,
                          activebackground=button_active_bg, activeforeground="white")
    toggle_btn.pack(fill=tk.X)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()



