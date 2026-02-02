# NSE Top Gainers & Top Losers – Simple Guide (Linux)

This project **downloads the list of top gaining and top losing stocks** from the National Stock Exchange (NSE) of India and saves them into two simple spreadsheet-style files that you can open in LibreOffice Calc, Google Sheets, or any spreadsheet app.

**You will get:**
- **topGainers.csv** – Stocks that went up the most today (with % change, prices, volume).
- **topLosers.csv** – Stocks that went down the most today (with % change, prices, volume).


---
## Part 1: If You Don’t Have Python Installed

The script runs on **Python**. If you’re not sure whether Python is installed, follow the steps in this section. If you already use Python, skip to **Part 2**.

### Step 1: Install Python (Ubuntu / Debian)

1. Open **Terminal** (search for “Terminal” in your applications, or press `Ctrl+Alt+T`).
2. Type the following and press **Enter** (you may be asked for your computer password):

   ```bash
   sudo apt-get update
   sudo apt-get install python3 python3-venv python3-pip
   ```

3. Wait until the installation finishes.

Then install the venv package if needed (name may vary, e.g. `python3-virtualenv` or `python3-venv`).

### Step 2: Check That Python Is Installed

1. Open **Terminal**.
2. Type:

   ```bash
   python3 --version
   ```

3. You should see something like `Python 3.12.x` or `Python 3.13.x`. If you see a version number, Python is installed. If you see “command not found”, repeat Step 1.

---

## Part 2: Setting Up This Project

### Step 1: Get the Project Folder on Your Computer

- If you already have the project: open the folder that contains `script.py` (and this Readme.md).
- If you received the project as a ZIP file: **right-click the ZIP → Extract Here** (or use “Extract” from the menu) to get a folder. Remember where this folder is (e.g. your home directory or Desktop).

We will call this folder the **“project folder.”** It should contain at least:
- `script.py`
- `Readme.md`

### Step 2: Open the Terminal in the Project Folder

You need to run commands **from inside the project folder**.

1. Open **Terminal**.
2. Go to the project folder. Type `cd` followed by a space, then either:
   - Type the full path, e.g. `cd /home/yourname/practice/stock_project`, or
   - Drag the project folder from your file manager into the Terminal window so the path appears after `cd `.
3. Press **Enter**. You are now “in” the project folder. You can check by typing `ls` and pressing Enter; you should see `script.py` and `Readme.md`.

### Step 3: Create a Virtual Environment

A “virtual environment” is an isolated space for this project so we don’t mix it with other software. You only need to do this once per project.

In the same Terminal window (and still inside the project folder), run:

```bash
python3 -m venv .venv
```

If you see an error like “python3-venv not found” or “No module named venv”, first install the venv package:

```bash
sudo apt-get install python3.13-venv
```

(Use your Python version number if different, e.g. `python3.12-venv`.)

After this, you should see a new folder named `.venv` inside your project folder. That’s correct.

### Step 4: Activate the Virtual Environment

Run:

```bash
source .venv/bin/activate
```

When it’s on, you’ll see something like `(.venv)` at the start of the line. That means you’re using the project’s environment.

### Step 5: Install the Required Library

In the same Terminal window, run:

```bash
pip install nsetools
```

Wait until it says “Successfully installed nsetools…”. You only need to do this once (unless you delete the `.venv` folder).

---

## Part 3: Running the Script and Getting Your Data

### Step 1: Run the Script

Make sure:
- You are in the **project folder** (see Part 2, Step 2).
- The virtual environment is **activated** (you see `(.venv)` in the prompt).

Then run:

```bash
python3 script.py
```

### Step 2: What Happens

- The script will connect to NSE and fetch the **current** top gainers and top losers.
- It may take a few seconds. You might not see any message; that’s normal.
- When the script finishes, it will return you to the prompt (no error message usually means success).

### Step 3: Where Are My Files?

Two new files (or updated files) will appear **in the same project folder**:

| File name        | What it contains                                      |
|------------------|--------------------------------------------------------|
| **topGainers.csv** | Top gaining stocks (name, % change, open/high/low, volume, etc.) |
| **topLosers.csv**  | Top losing stocks (same type of information)          |

**Note:** Each time you run the script, it **adds** new rows to these files. So you may see multiple header rows if you run it many times. For a clean sheet, you can delete the old CSV files and run the script again to get a fresh set.

### Step 4: Opening the CSV Files on Linux

**In LibreOffice Calc:**
1. Open **LibreOffice Calc** (or open LibreOffice and choose “Spreadsheet”).
2. Go to **File → Open** and browse to your project folder.
3. Select **topGainers.csv** or **topLosers.csv**.
4. If asked, set the separator to **Comma** and click **OK**. You’ll see columns like: Stock name, % change, Open price, High price, Low price, Previous price, Volume, Ltp.

**In Google Sheets (in a browser):**
1. Go to https://sheets.google.com and open a new blank sheet.
2. Go to **File → Import → Upload** and select **topGainers.csv** or **topLosers.csv** from your project folder.
3. Choose “Replace spreadsheet” or “Insert new sheet(s)” and set the separator to **Comma**. Click **Import data**.

You can now sort, filter, or use the data like any normal spreadsheet.

---

## Quick Reference: Running Again Next Time

Once setup is done, next time you only need to:

1. Open **Terminal**.
2. Go to the project folder, for example:
   ```bash
   cd ~/practice/stock_project
   ```
3. Activate the environment:
   ```bash
   source .venv/bin/activate
   ```
4. Run the script:
   ```bash
   python3 script.py
   ```
5. Open **topGainers.csv** and **topLosers.csv** from the project folder in LibreOffice Calc or Google Sheets.

---

## What the Columns Mean (Simple Explanation)

| Column          | Meaning in simple words |
|-----------------|--------------------------|
| **Stock name**  | Short code of the company (e.g. RELIANCE, TCS). |
| **% change**    | How much the price went up or down in percentage compared to the previous close. |
| **Open price**  | Price when the market opened today. |
| **High price**  | Highest price reached today. |
| **Low price**   | Lowest price reached today. |
| **Previous price** | Last closing price (previous day). |
| **Volume**      | How many shares were traded today. |
| **Ltp**         | Last Traded Price – the latest price at which the stock was bought/sold. |

---

## Troubleshooting (Linux)

**“python3” not found**  
- Python is not installed. Go back to **Part 1** and run the `sudo apt-get install ...` (or equivalent) commands for your Linux distribution.

**“python3-venv not found” or “No module named venv”**  
- Install the venv package, for example: `sudo apt-get install python3.13-venv` (use your Python version number, e.g. 3.12).

**“pip” not found or “externally-managed-environment”**  
- Use the **virtual environment** (Part 2, Steps 3 and 4). After activating with `source .venv/bin/activate`, run `pip install nsetools` again.

**“No module named nsetools”**  
- The library wasn’t installed. Make sure the virtual environment is **activated** (you see `(.venv)` in the prompt), then run `pip install nsetools` again.

**Script runs but I don’t see any CSV files**  
- Check that you’re looking in the **same folder** where `script.py` is. The CSV files are created there. Use your file manager or `ls` in the project folder to confirm.

**I get an error about “list index out of range”**  
- The script is already updated to handle cases when NSE returns fewer stocks. Make sure you’re using the latest `script.py` from this project.

**Data looks old or wrong**  
- The script fetches **live** data from NSE at the time you run it. Run it during or shortly after market hours (NSE India) for current data. Outside market hours, you may get the last available snapshot.

---

## Summary

- **First time (Linux):** Install Python and venv (Part 1) → Put project in a folder (Part 2) → Open Terminal in that folder → Create virtual environment (`python3 -m venv .venv`) → Activate it (`source .venv/bin/activate`) → Run `pip install nsetools` → Run `python3 script.py`.
- **Output:** **topGainers.csv** and **topLosers.csv** in the project folder, with stock names, % change, and price/volume info. Open them in LibreOffice Calc or Google Sheets.
- **Next times:** Open Terminal → go to project folder (`cd ...`) → run `source .venv/bin/activate` → run `python3 script.py`.

If you follow the steps in order, you can use this project on Linux even if you’ve never used Python or the command line before.
