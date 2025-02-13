# HP 12C Learning Objectives: Present and Future Value Calculations

## Key Concepts:
1. **Present Value (PV)**: The current value of future cash flows, discounted at a given interest rate.
2. **Future Value (FV)**: The value of an investment at a future date, based on a given interest rate.
3. **Ordinary Annuity**: Payments occur at the **end** of each period.
4. **Annuity Due**: Payments occur at the **beginning** of each period.

---

## HP 12C Steps:

### 1. **Clear the Calculator**:
   - Press `f` + `CLX` to clear all previous entries.

### 2. **Set Payment Timing**:
   - For **Ordinary Annuity (END mode)**: Default (no action needed).
   - For **Annuity Due (BEGIN mode)**: Press `g` + `BEG` ("BEGIN" will appear).

### 3. **Enter Values**:
   - Number of periods: Enter value, press `n`.
   - Interest rate: Enter value, press `i`.
   - Payment amount: Enter value, press `PMT`.

### 4. **Calculate**:
   - For **Present Value (PV)**: Press `PV`.
   - For **Future Value (FV)**: Press `FV`.

---

## Example: Present Value of an Annuity Due
- Payments: $200,000/year for 20 years, starting today.
- Interest rate: 7%.
- Steps:
  1. Clear: `f` + `CLX`.
  2. Set BEGIN mode: `g` + `BEG`.
  3. Enter `20`, press `n`.
  4. Enter `7`, press `i`.
  5. Enter `200000`, press `PMT`.
  6. Press `PV` to calculate.
- Result: PV = $2,262,038.33.

---

## Key Takeaways:
- Use **BEGIN mode** for payments at the start of each period.
- Use **END mode** for payments at the end of each period.
- Always clear the calculator before starting a new calculation.

### How to Calculate CAGR on the HP 12C

#### Steps:
1. **Clear the calculator:**  
   Press **f** (the gold key) and then **CLEAR FIN** to clear all financial registers.

2. **Enter the Ending Value (FV):**  
   Input the ending value (e.g., 2017 sales or net profit) and press **FV**.

3. **Enter the Beginning Value (PV):**  
   Input the beginning value (e.g., 2012 sales or net profit), press **CHS** (to make it negative), and then press **PV**.

4. **Enter the Number of Years (n):**  
   Input the number of years (e.g., 5) and press **n**.

5. **Calculate the CAGR:**  
   Press **i** to compute the annual growth rate.

---

#### Key Terms:
- **CHS:**  
   Stands for "Change Sign." It is used to make a value negative. In CAGR calculations, **PV** (beginning value) must be negative to comply with the HP 12C's cash flow convention.

- **CAGR (Compound Annual Growth Rate):**  
   A measure of the average annual growth rate of an investment or metric over a specified period, assuming the growth happens at a constant rate.

---

#### Why is PV Negative on the HP 12C?
- **Cash Flow Convention:**  
   The HP 12C treats **PV** (present value) as an outflow (negative) and **FV** (future value) as an inflow (positive). This is a native feature of the calculator, designed to align with financial calculations where cash flows have direction (e.g., investments are outflows, and returns are inflows).

- **Mathematical Context:**  
   In the CAGR formula:  
   \[
   \text{CAGR} = \left( \frac{\text{FV}}{\text{PV}} \right)^{\frac{1}{n}} - 1
   \]  
   The HP 12C uses the **i** (interest rate) function, which assumes **PV** is negative to represent an initial investment or cost. This ensures the calculator interprets the cash flow direction correctly.

---

### Example:
#### Sales Growth Rate (2012–2017):
- **Ending Value (FV):** ₩19,166.0 billion  
- **Beginning Value (PV):** ₩14,146.4 billion (input as negative using **CHS**)  
- **Number of Years (n):** 5  

Result: **Sales CAGR ≈ 6.26%**

#### Net Profit Growth Rate (2012–2017):
- **Ending Value (FV):** ₩727.5 billion  
- **Beginning Value (PV):** ₩796.4 billion (input as negative using **CHS**)  
- **Number of Years (n):** 5  

Result: **Net Profit CAGR ≈ -1.79%** (negative growth)

---

### Copyable HP 12C Keystrokes:
#### Sales CAGR:
1. **f** → **CLEAR FIN**  
2. `19166` → **FV**  
3. `14146.4` → **CHS** → **PV**  
4. `5` → **n**  
5. **i**  

#### Net Profit CAGR:
1. **f** → **CLEAR FIN**  
2. `727.5` → **FV**  
3. `796.4` → **CHS** → **PV**  
4. `5` → **n**  
5. **i**  