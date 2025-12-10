# Digital-Workflow-for-Patient-Specific-Parametric-Prosthetic-Foot-Design
This project automates the customisation of a parametric prosthetic foot model using Python and Autodesk Fusion 360. User-defined size presets or custom dimensions are exported as synchronised parameters and applied directly to the CAD model, enabling fast, repeatable, and patient-specific geometry updates without manual redesign.

HOW TO USE THIS PROJECT
This project links a Python script (Google Colab) with a parametric prosthetic foot model in Autodesk Fusion 360 via a CSV-based digital workflow. The Python code generates parameter values (P1–P9) and Fusion updates the CAD model automatically.

1. Set up the Parametric CAD Model (Fusion 360)
- Open your prosthetic foot design in Fusion 360.
- Go to: Modify → Change Parameters
- Under User Parameters, create (or confirm) the parameters: P1, P2, P3, P4, P5, P6, P7, P8, P9
- Make sure your key dimensions (lengths, offsets, angles etc.) are driven by these user parameters
- Save the design. Once this is done, changing P1-P9 in Change Parameters should update the prosthetic geometry

2. Run the Python Code (Google Colab used)
- Open a Google Colab notebook
- Input the code in a single cell, run.
- When prompted, either:
         - Enter a size label (XS, S, M, L, or XL)
         - Enter a cusomt main size (P1) in cm
- The script will:
         - Compute all parameters P1-P9 based on your choice
         - Generate a Fusion-compatible CSV
         - Automatically a trigger a download of the CSV to your computer

3. import Parameters into Fusion 360
- In Fusion 360, open your prosthetic model
- Go to: Modify → Change Parameters
- Click Import (top-right of the Parameters dialog).
- Select the downloaded CSV file and Click OK.
- The model will be rebuilt

4. Iterating with Different Sizes
- To generate new prosthetic variants:
          - Re-run the input cell in the Colab notebook.
          - Enter a new size (e.g. XL, S) or new custom P1.
          - Download the new CSV.
          - Re-import it into Fusion 360 as before.
  
