
# **Password Generator GUI Application**

## **Overview**
This Python application is a **Graphical User Interface (GUI)** tool for generating random passwords. Users can customize various password features, such as the inclusion of uppercase letters, lowercase letters, numbers, symbols, and spaces, as well as define the password length.

The tool provides options to:
- Generate a random password based on the selected features.
- Save the generated password to a file.
- Restart the application or reset the settings.
- Exit the application gracefully.

---

## **Features**
- **Customizable Password Options**:
  - Include/exclude uppercase, lowercase, numbers, symbols, or spaces.
- **Password Length**:
  - Choose a length between 4 and 20 characters.
- **Save Passwords**:
  - Automatically save generated passwords to a text file (`passwords.txt`).
- **User-Friendly Interface**:
  - Intuitive buttons (`yes`/`no`) for toggling features.
  - Real-time password display with centered formatting.
- **Keyboard Shortcuts**:
  - `<Enter>`: Generate a password.
  - `<r>`: Restart the application.
  - `<q>`: Quit the application.

---

## **Requirements**
### **Dependencies**
- Python 3.6 or higher
- **Libraries**:
  - `tkinter` (standard Python library for GUI development)
  - `ttk` (themed widgets from tkinter)
  - `subprocess` (for restarting the application)
  - `sys` (for exiting the application)
- **External Files**:
  - `generate_password_functions.py`: Contains the password generation logic.
  - `errors.py`: Defines custom exceptions, specifically `LengthLimitError`.

---

## **Setup and Installation**
1. **Clone the Repository**:
   ```bash
   git clone <https://github.com/EhsanDrn2207/Generate_Random_Password_GUI.git>
   cd <Generate_Random_Password_GUI>
   ```

2. **Ensure Dependencies Are Installed**:
   - Make sure Python 3.6+ is installed.
   - No additional Python libraries are needed as `tkinter` and `ttk` are included in the Python standard library.

3. **Add External Modules**:
   - Ensure `generate_password_functions.py` and `errors.py` are in the same directory as the main script.

4. **Add the Icon File (Optional)**:
   - Place an icon file named `pattern.ico` in an `image` folder within the project directory. This is used as the application icon.

---

## **How to Run**
Run the script using the following command:
```bash
python password_generator_app.py
```

---

## **Usage Instructions**
### **1. Customize Password Settings**
- Use the `yes`/`no` buttons next to each feature to include or exclude it from the password:
  - **UpperCase**: Includes uppercase letters.
  - **LowerCase**: Includes lowercase letters.
  - **Number**: Includes numbers.
  - **Symbol**: Includes special characters (e.g., `@`, `!`).
  - **Space**: Includes spaces.

### **2. Set Password Length**
- Enter a value (between 4 and 20) in the **Length** field. If no value is provided, a default length of 8 is used.

### **3. Generate a Password**
- Press the `run` button or hit `<Enter>` to generate a password.
- The password will be displayed in the center of the app window.

### **4. Save Passwords**
- The generated password is automatically saved to `passwords.txt`.

### **5. Restart or Quit**
- **Restart**: Press the `reset` button or hit `<r>` to restart the application.
- **Quit**: Press the `quit` button or hit `<q>` to close the app.

---

## **File Structure**
```
project/
│
├── password_generator_app.py      # Main application script
├── generate_password_functions.py # Password generation logic (external module)
├── errors.py                      # Custom error definitions (external module)
├── passwords.txt                  # File where passwords are saved
├── README.md                      # Project documentation
└── image/
    └── pattern.ico                # Application icon (optional)
```

---

## **Customization**
- **Default Settings**:
  Modify the `self.defual_setting_dict` dictionary in the `__init__` method to change the default password configuration:
  ```python
  self.defual_setting_dict = {
      "UpperCase": True,
      "LowerCase": False,
      "Number": True,
      "Symbol": True,
      "Space": False
  }
  ```

- **Default Password Length**:
  The default length (8) can be changed by modifying the logic in the `generate_random_password_gui` method:
  ```python
  length = self.length_ent.get() or 8
  ```

---

## **Error Handling**
1. **Invalid Length**:
   - If the user enters a length less than 4 or greater than 20, a custom `LengthLimitError` is raised.
   - A message (`"Length: 4 to 20"`) is displayed to guide the user.

2. **Default Fallback**:
   - If no length is provided or the input is invalid, the default length of 8 is used.

---

## **Keyboard Shortcuts**
- `<Enter>`: Generate a password.
- `<q>`: Quit the application.
- `<r>`: Restart the application.

---

## **Contributing**
Contributions are welcome! If you’d like to improve this project:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.
