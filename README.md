# Eraysr: Secure File Overwriting and Deletion, with Simulate Option

## **About**
Eraysr is a Python-based tool designed to help users simulate the secure erasure of files and directories. It is particularly useful for scenarios such as:
- Safely handling temporary files, including sensitive documents.
- Preparing devices for repurposing or disposal.
- Practicing or testing secure deletion processes without affecting actual data.

This repository includes code that demonstrates how to simulate file overwrites, providing a clear understanding of the process without modifying any data.

---

## **Features**
- **Simulated File Overwriting:** Prints file metadata and progress statements during simulated overwrite passes.
- **Directory-Wide Simulation:** Processes all files in a specified directory.
- **Customizable Passes:** Users can specify the number of overwrite passes for the simulation.

---

## **Usage**

### **Prerequisites**
- Python 3.x installed on your machine.
- Basic understanding of Python and file system operations.

### **Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/DavidEaton/Eraysr.git
   cd Eraysr
   ```

2. Edit the script to specify your target directory. Replace:
   ```python
   directory_path = "C:\\Users\\HoobaLou\\Pictures"
   ```
   with the path to your desired directory.

3. Run the script:
   ```bash
   python fake_overwrite_file.py
   ```

4. Observe the simulation output, including file size, modification date, and progress for each pass.

---

## **Example Output**
When the script is run, you will see progress statements like:
```
Starting overwrite simulation for: C:\Users\HoobaLou\Pictures\example.jpg
File size: 123456 bytes
Last modified: Thu Nov 16 10:30:00 2023
Pass 1/3: Simulating overwrite...
Pass 2/3: Simulating overwrite...
Pass 3/3: Simulating overwrite...
Pretend deletion complete for: C:\Users\HoobaLou\Pictures\example.jpg
==================================================
```

---

## **Why Simulate?**
Simulating the secure deletion of files is useful for:
- **Education:** Learning about secure file deletion techniques.
- **Testing:** Verifying logic and behavior of deletion scripts without impacting data.
- **Development:** Debugging file processing code in a safe environment.

---

## **Future Enhancements**
Planned updates include:
- Actual secure deletion functionality with data overwriting.
- Advanced file filtering options.
- User-friendly logging and reporting.

---

## **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or suggestions.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

## **Acknowledgments**
Thank you for exploring this project! Feedback and contributions are always appreciated. 😊
