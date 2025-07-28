import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox
from textwrap import dedent
from pathlib import Path
import subprocess
import shutil


class TravelReportGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel Report Generator")
        self.root.geometry("600x800")

        # Create main frame with scrollbar
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Create canvas and scrollbar
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Bind mousewheel to canvas
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

        self.create_widgets(scrollable_frame)

    def create_widgets(self, parent):
        # Title
        title_label = ttk.Label(
            parent, 
            text="TRAVEL REPORT GENERATOR", 
            font=("consolas", 20, "bold")
        )
        title_label.pack(pady=(20, 20))

    # Basic Information Section
        basic_frame = ttk.LabelFrame(parent, text="Basic Information", padding="10")
        basic_frame.pack(fill='both', pady=(0, 10))
        # Destination
        ttk.Label(basic_frame, font=('consolas', 12), text="Destination:").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        self.destination_var = tk.StringVar(value="Your Destination")
        ttk.Entry(basic_frame, font=('consolas', 12), textvariable=self.destination_var, width=30,).grid(
            row=0, column=1, padx=(10, 0), pady=2
        )

        # Number of people
        ttk.Label(basic_frame, font=('consolas', 12), text="Number of People:").grid(
            row=1, column=0, sticky=tk.W, pady=2
        )
        self.number_of_people_var = tk.IntVar(value=1)
        ttk.Entry(basic_frame, font=('consolas', 12), textvariable=self.number_of_people_var, width=30).grid(
            row=1, column=1, padx=(10, 0), pady=2
        )

        # Number of nights
        ttk.Label(basic_frame, font=('consolas', 12), text="Number of Nights:").grid(
            row=2, column=0, sticky=tk.W, pady=2
        )
        self.number_of_nights_var = tk.IntVar(value=1)
        ttk.Entry(basic_frame, font=('consolas', 12), textvariable=self.number_of_nights_var, width=30).grid(
            row=2, column=1, padx=(10, 0), pady=2
        )

        # Desire level to visit
        ttk.Label(basic_frame, font=('consolas', 12), text="Desire Level to Visit (total):").grid(
            row=3, column=0, sticky=tk.W, pady=2
        )
        self.desire_lv_to_visit_var = tk.IntVar(value=5)
        ttk.Entry(basic_frame, font=('consolas', 12), textvariable=self.desire_lv_to_visit_var, width=30).grid(
            row=3, column=1, padx=(10, 0), pady=2
        )

    # Dates Section
        dates_frame = ttk.LabelFrame(parent, text="Travel Dates", padding="10")
        dates_frame.pack(fill='both', pady=(0, 10))

        # Departure date
        ttk.Label(dates_frame, font=('consolas', 12), text="Departure Date:").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        self.departure_date_var = tk.StringVar(value='26/06/1992')
        ttk.Entry(dates_frame, font=('consolas', 12), textvariable=self.departure_date_var, width=30).grid(
            row=0, column=1, padx=(10, 0), pady=2
        )

        # Return date
        ttk.Label(dates_frame, font=('consolas', 12), text="Return Date:").grid(
            row=1, column=0, sticky=tk.W, pady=2
        )
        self.return_date_var = tk.StringVar(value='14/09/1996')
        ttk.Entry(dates_frame, font=('consolas', 12), textvariable=self.return_date_var, width=30).grid(
            row=1, column=1, padx=(10, 0), pady=2
        )

    # Outward Journey Section
        outward_frame = ttk.LabelFrame(parent, text="Outward Journey", padding="10")
        outward_frame.pack(fill='both', pady=(0, 10))

        # Departure airport outward
        ttk.Label(outward_frame, font=('consolas', 12), text="Departure Airport:").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        self.departure_airport_outward_var = tk.StringVar(value='From')
        ttk.Entry(
            outward_frame, font=('consolas', 12), textvariable=self.departure_airport_outward_var, width=30
        ).grid(row=0, column=1, padx=(10, 0), pady=2)

        # Departure time outward
        ttk.Label(outward_frame, font=('consolas', 12), text="Departure Time:").grid(
            row=1, column=0, sticky=tk.W, pady=2
        )
        self.departure_time_outward_var = tk.StringVar(value='00:00')
        ttk.Entry(
            outward_frame, font=('consolas', 12), textvariable=self.departure_time_outward_var, width=30
        ).grid(row=1, column=1, padx=(10, 0), pady=2)

        # Arrival airport outward
        ttk.Label(outward_frame, font=('consolas', 12), text="Arrival Airport:").grid(
            row=2, column=0, sticky=tk.W, pady=2
        )
        self.arrival_airport_outward_var = tk.StringVar(value="To")
        ttk.Entry(
            outward_frame, font=('consolas', 12), textvariable=self.arrival_airport_outward_var, width=30
        ).grid(row=2, column=1, padx=(10, 0), pady=2)

        # Arrival time outward
        ttk.Label(outward_frame, font=('consolas', 12), text="Arrival Time:").grid(
            row=3, column=0, sticky=tk.W, pady=2
        )
        self.arrival_time_outward_var = tk.StringVar(value='00:00')
        ttk.Entry(
            outward_frame, font=('consolas', 12), textvariable=self.arrival_time_outward_var, width=30
        ).grid(row=3, column=1, padx=(10, 0), pady=2)

        # Price outward
        ttk.Label(outward_frame, font=('consolas', 12), text="Price (€):").grid(
            row=4, column=0, sticky=tk.W, pady=2
        )
        self.price_outward_var = tk.DoubleVar(value=0.0)
        ttk.Entry(outward_frame, font=('consolas', 12), textvariable=self.price_outward_var, width=30).grid(
            row=4, column=1, padx=(10, 0), pady=2
        )

    # Return Journey Section
        return_frame = ttk.LabelFrame(parent, text="Return Journey", padding="10")
        return_frame.pack(fill='both', pady=(0, 10))

        # Departure airport return
        ttk.Label(return_frame, font=('consolas', 12), text="Departure Airport:").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        self.departure_airport_return_var = tk.StringVar(value='From')
        ttk.Entry(
            return_frame, font=('consolas', 12), textvariable=self.departure_airport_return_var, width=30
        ).grid(row=0, column=1, padx=(10, 0), pady=2)

        # Departure time return
        ttk.Label(return_frame, font=('consolas', 12), text="Departure Time:").grid(
            row=1, column=0, sticky=tk.W, pady=2
        )
        self.departure_time_return_var = tk.StringVar(value='00:00')
        ttk.Entry(
            return_frame, font=('consolas', 12), textvariable=self.departure_time_return_var, width=30
        ).grid(row=1, column=1, padx=(10, 0), pady=2)

        # Arrival airport return
        ttk.Label(return_frame, font=('consolas', 12), text="Arrival Airport:").grid(
            row=2, column=0, sticky=tk.W, pady=2
        )
        self.arrival_airport_return_var = tk.StringVar(value='To')
        ttk.Entry(
            return_frame, font=('consolas', 12), textvariable=self.arrival_airport_return_var, width=30
        ).grid(row=2, column=1, padx=(10, 0), pady=2)

        # Arrival time return
        ttk.Label(return_frame, font=('consolas', 12), text="Arrival Time:").grid(
            row=3, column=0, sticky=tk.W, pady=2
        )
        self.arrival_time_return_var = tk.StringVar(value='00:00')
        ttk.Entry(
            return_frame, font=('consolas', 12), textvariable=self.arrival_time_return_var, width=30
        ).grid(row=3, column=1, padx=(10, 0), pady=2)

        # Price return
        ttk.Label(return_frame, font=('consolas', 12), text="Price (€):").grid(
            row=4, column=0, sticky=tk.W, pady=2
        )
        self.price_return_var = tk.DoubleVar(value=0.0)
        ttk.Entry(return_frame, font=('consolas', 12), textvariable=self.price_return_var, width=30).grid(
            row=4, column=1, padx=(10, 0), pady=2
        )

    # Costs Section
        costs_frame = ttk.LabelFrame(parent, text="Additional Costs", padding="10")
        costs_frame.pack(fill='both', pady=(0, 10))

        # Baggage cost
        ttk.Label(costs_frame, font=('consolas', 12), text="Baggage Cost (€):").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        self.baggage_cost_var = tk.DoubleVar(value=0.0)
        ttk.Entry(costs_frame, font=('consolas', 12), textvariable=self.baggage_cost_var, width=30).grid(
            row=0, column=1, padx=(10, 0), pady=2
        )

        # Average nightly cost
        ttk.Label(costs_frame, font=('consolas', 12), text="Average Nightly Cost (€):").grid(
            row=1, column=0, sticky=tk.W, pady=2
        )
        self.avg_nightly_cost_var = tk.DoubleVar(value=0.0)
        ttk.Entry(costs_frame, font=('consolas', 12), textvariable=self.avg_nightly_cost_var, width=30).grid(
            row=1, column=1, padx=(10, 0), pady=2
        )

        # Car rental cost
        ttk.Label(costs_frame, font=('consolas', 12), text="Car Rental Cost (€):").grid(
            row=2, column=0, sticky=tk.W, pady=2
        )
        self.car_rental_cost_var = tk.DoubleVar(value=0.0)
        ttk.Entry(costs_frame, font=('consolas', 12), textvariable=self.car_rental_cost_var, width=30).grid(
            row=2, column=1, padx=(10, 0), pady=2
        )

        # Home airport journey cost
        ttk.Label(costs_frame, font=('consolas', 12), text="Home-Airport Journey Cost (€):").grid(
            row=3, column=0, sticky=tk.W, pady=2
        )
        self.home_airport_journey_cost_var = tk.DoubleVar(value=0.0)
        ttk.Entry(
            costs_frame, font=('consolas', 12), textvariable=self.home_airport_journey_cost_var, width=30
        ).grid(row=3, column=1, padx=(10, 0), pady=2)

    # Notes Section
        notes_frame = ttk.LabelFrame(parent, text="Notes (Optional)", padding="10")
        notes_frame.pack(fill='both', pady=(0, 10))

        self.notes_text = tk.Text(notes_frame, font=('consolas', 12), height=4, width=60)
        self.notes_text.pack(fill=tk.X)

    # Output Options Section
        output_frame = ttk.LabelFrame(parent, text="", padding="0")
        output_frame.pack(fill='both', pady=(0, 10))

    # File format selection
        ttk.Label(output_frame, font=('consolas', 12), text="Output Format:").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        self.output_format_var = tk.StringVar(value="markdown")
        format_frame = ttk.Frame(output_frame)
        format_frame.grid(row=0, column=1, padx=(10, 0), pady=0, sticky=tk.W)

        ttk.Radiobutton(
            format_frame,
            text="Markdown",
            variable=self.output_format_var,
            value="markdown",
        ).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Radiobutton(
            format_frame, text="PDF", variable=self.output_format_var, value="pdf"
        ).pack(side=tk.LEFT)

        # Generate Button
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X, pady=(20, 0))

        generate_btn = ttk.Button(
            button_frame,
            text="Generate Report",
            command=self.generate_report,
            style="Accent.TButton",
        )
        generate_btn.pack(pady=10)

    # Merge Reports Section
        merge_frame = ttk.LabelFrame(parent, text="Merge Reports", padding="10")
        merge_frame.pack(fill=tk.X, pady=(10, 0))

        # Output filename for merged report
        ttk.Label(merge_frame, font=('consolas', 12), text="Merged Report Name:").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        self.merged_filename_var = tk.StringVar(value="travel_report")
        ttk.Entry(merge_frame, font=('consolas', 12), textvariable=self.merged_filename_var, width=30).grid(
            row=0, column=1, padx=(10, 0), pady=2
        )

        # Merge format selection
        ttk.Label(merge_frame, font=('consolas', 12), text="Merge Format:").grid(
            row=1, column=0, sticky=tk.W, pady=2
        )
        self.merge_format_var = tk.StringVar(value="markdown")
        merge_format_frame = ttk.Frame(merge_frame)
        merge_format_frame.grid(row=1, column=1, padx=(10, 0), pady=2, sticky=tk.W)

        ttk.Radiobutton(
            merge_format_frame,
            text="Markdown",
            variable=self.merge_format_var,
            value="markdown",
        ).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Radiobutton(
            merge_format_frame, text="PDF", variable=self.merge_format_var, value="pdf"
        ).pack(side=tk.LEFT)

        # Merge Button
        merge_btn = ttk.Button(
            merge_frame, text="Merge All Reports", command=self.merge_reports
        )
        merge_btn.grid(row=2, column=0, columnspan=2, pady=10)

    def generate_report(self):
        try:
            # Validate required fields
            if not self.destination_var.get().strip():
                messagebox.showerror("Error", "Destination is required!")
                return

            # Create parameters object
            params = type("Params", (), {})()
            params.destination = self.destination_var.get().strip()
            params.number_of_people = self.number_of_people_var.get()
            params.number_of_nights = self.number_of_nights_var.get()
            params.desire_lv_to_visit = self.desire_lv_to_visit_var.get()
            params.departure_date = self.departure_date_var.get().strip()
            params.return_date = self.return_date_var.get().strip()
            params.departure_airport_outward_journey = (
                self.departure_airport_outward_var.get().strip()
            )
            params.departure_time_outward_journey = (
                self.departure_time_outward_var.get().strip()
            )
            params.arrival_airport_outward_journey = (
                self.arrival_airport_outward_var.get().strip()
            )
            params.arrival_time_outward_journey = (
                self.arrival_time_outward_var.get().strip()
            )
            params.price_outward_journey = self.price_outward_var.get()
            params.departure_airport_return_journey = (
                self.departure_airport_return_var.get().strip()
            )
            params.departure_time_return_journey = (
                self.departure_time_return_var.get().strip()
            )
            params.arrival_airport_return_journey = (
                self.arrival_airport_return_var.get().strip()
            )
            params.arrival_time_return_journey = (
                self.arrival_time_return_var.get().strip()
            )
            params.price_return_journey = self.price_return_var.get()
            params.baggage_cost = self.baggage_cost_var.get()
            params.avg_nightly_cost = self.avg_nightly_cost_var.get()
            params.car_rental_cost = self.car_rental_cost_var.get()
            params.home_airport_journey_cost = self.home_airport_journey_cost_var.get()
            params.notes = self.notes_text.get("1.0", tk.END).strip() or None

            # Generate the report
            if self.output_format_var.get() == "markdown":
                self.generate_markdown(params)
            else:
                self.generate_pdf(params)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def generate_markdown(self, params):
        content = self.generate_content(params)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        reports_dir = os.path.join(current_dir, "reports")
        Path(reports_dir).mkdir(parents=True, exist_ok=True)
        file_name = f"{params.destination}.md"

        with open(os.path.join(reports_dir, file_name), "w", encoding="utf-8") as f:
            f.write(content)

        messagebox.showinfo("Success", f"{file_name} generated successfully!")

    def generate_pdf(self, params):
        try:
            # Check if pandoc is available
            if not self.check_pandoc():
                messagebox.showerror(
                    "Error",
                    "Pandoc is not installed or not found in PATH.\n"
                    "Please install pandoc to generate PDF files.\n"
                    "Visit: https://pandoc.org/installing.html",
                )
                return

            # First generate markdown content
            content = self.generate_content(params)

            # Create reports directory
            current_dir = os.path.dirname(os.path.abspath(__file__))
            reports_dir = os.path.join(current_dir, "reports")
            Path(reports_dir).mkdir(parents=True, exist_ok=True)

            # Create temporary markdown file
            temp_md_file = os.path.join(reports_dir, f"{params.destination}_temp.md")
            with open(temp_md_file, "w", encoding="utf-8") as f:
                f.write(content)

            # Convert to PDF using pandoc
            pdf_file = os.path.join(reports_dir, f"{params.destination}.pdf")

            try:
                # Use absolute paths and proper command structure
                cmd = [
                    "pandoc",
                    temp_md_file,
                    "-o",
                    pdf_file,
                    "--pdf-engine=pdflatex",
                    "--variable=geometry:margin=1in",
                ]

                result = subprocess.run(cmd, check=True, capture_output=True, text=True)

                # Clean up temporary file
                if os.path.exists(temp_md_file):
                    os.remove(temp_md_file)

                if os.path.exists(pdf_file):
                    messagebox.showinfo(
                        "Success", f"{params.destination}.pdf generated successfully!"
                    )
                else:
                    messagebox.showerror(
                        "Error", "PDF file was not created successfully."
                    )

            except subprocess.CalledProcessError as e:
                # Clean up temporary file
                if os.path.exists(temp_md_file):
                    os.remove(temp_md_file)

                error_msg = (
                    f"PDF generation failed.\nError: {e.stderr if e.stderr else str(e)}"
                )
                messagebox.showerror("Error", error_msg)

        except Exception as e:
            messagebox.showerror("Error", f"PDF generation failed: {str(e)}")

    def check_pandoc(self):
        """Check if pandoc is installed and available"""
        try:
            result = subprocess.run(
                ["pandoc", "--version"], capture_output=True, text=True, check=True
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def merge_reports(self):
        """Merge all markdown reports into a single file"""
        try:
            output_filename = self.merged_filename_var.get().strip()
            if not output_filename:
                output_filename = "travel_report"

            current_dir = os.path.dirname(os.path.abspath(__file__))
            merged_dir = os.path.join(current_dir, "merged")
            reports_dir = os.path.join(current_dir, "reports")

            # Create directories if they don't exist
            Path(merged_dir).mkdir(parents=True, exist_ok=True)
            Path(reports_dir).mkdir(parents=True, exist_ok=True)

            # Find all markdown files in reports directory
            md_files = [
                f
                for f in os.listdir(reports_dir)
                if f.endswith(".md") and not f.startswith(output_filename)
            ]

            if not md_files:
                messagebox.showwarning(
                    "Warning", "No markdown files found in reports directory!"
                )
                return

            # Sort files for consistent ordering
            md_files.sort()

            # Create merged content
            merged_content = ""
            for filename in md_files:
                filepath = os.path.join(reports_dir, filename)
                with open(filepath, "r", encoding="utf-8") as infile:
                    merged_content += infile.read()
                    merged_content += "\n___\n\n"  # Add separator between reports

            # Generate output based on selected format
            if self.merge_format_var.get() == "markdown":
                output_file = os.path.join(merged_dir, f"{output_filename}.md")
                with open(output_file, "w", encoding="utf-8") as outfile:
                    outfile.write(merged_content)
                messagebox.showinfo(
                    "Success", f"Merged report saved as: {output_filename}.md"
                )

            else:  # PDF format
                if not self.check_pandoc():
                    messagebox.showerror(
                        "Error",
                        "Pandoc is not installed or not found in PATH.\n"
                        "Please install pandoc to generate PDF files.",
                    )
                    return

                # Create temporary markdown file
                temp_md_file = os.path.join(merged_dir, f"{output_filename}_temp.md")
                with open(temp_md_file, "w", encoding="utf-8") as outfile:
                    outfile.write(merged_content)

                # Convert to PDF
                pdf_file = os.path.join(merged_dir, f"{output_filename}.pdf")

                try:
                    cmd = [
                        "pandoc",
                        temp_md_file,
                        "-o",
                        pdf_file,
                        "--pdf-engine=pdflatex",
                        "--variable=geometry:margin=1in",
                    ]

                    subprocess.run(cmd, check=True, capture_output=True, text=True)

                    # Clean up temporary file
                    if os.path.exists(temp_md_file):
                        os.remove(temp_md_file)

                    if os.path.exists(pdf_file):
                        messagebox.showinfo(
                            "Success",
                            f"Merged PDF report saved as: {output_filename}.pdf",
                        )
                    else:
                        messagebox.showerror(
                            "Error", "Merged PDF file was not created successfully."
                        )

                except subprocess.CalledProcessError as e:
                    # Clean up temporary file
                    if os.path.exists(temp_md_file):
                        os.remove(temp_md_file)

                    error_msg = f"PDF generation failed.\nError: {e.stderr if e.stderr else str(e)}"
                    messagebox.showerror("Error", error_msg)

        except Exception as e:
            messagebox.showerror("Error", f"Merge operation failed: {str(e)}")

    def render_baggage(self, params):
        value = f"#### Bagaglio  \n\t10kg: {params.baggage_cost}€  \n"
        return dedent(value) if params.baggage_cost else ""
    
    def render_avg_night_cost(self, params):
        value =  f"#### Costo Medio a notte  \n\t{params.avg_nightly_cost}€ per {params.number_of_people} persone.  \n"
        return dedent(value) if params.avg_nightly_cost else ""

    def render_car_rental(self, params):
        value = f"#### Costo Noleggio Veicolo  \n\t{params.car_rental_cost}€ per {params.number_of_nights - 1 } giorni. \n"
        return dedent(value) if params.car_rental_cost else ""

    def render_home_airport(self, params):
        value =  f"#### Costo Tragitto Casa Aeroporto  \n\t{params.home_airport_journey_cost}€ treno o auto + casello + taxi o bus o navette varie.  \n"
        return dedent(value) if params.home_airport_journey_cost else ""

    def render_notes(self, params):
        value = f"__Notes__:  \n>{params.notes}\n"
        return dedent(value) if params.notes else ""
    
    def render_totals(self, params):
        tot = round(
            (params.avg_nightly_cost * params.number_of_nights)
            + params.car_rental_cost
            + params.price_outward_journey
            + params.price_return_journey
            + params.home_airport_journey_cost,
            2,
        )
        per_person = round(tot / params.number_of_people, 2)
        per_person_per_night =  round(per_person / params.number_of_nights, 2)

        return f"#### Costi per {params.number_of_nights} notti  \n\tTotale: {tot}€  \n\tTot a persona: {per_person}€  \n\tTot a notte per persona : {per_person_per_night}€"
    
    def render_desire(self, params):
        desire_to_visit = params.desire_lv_to_visit / params.number_of_people
        return f"*Voglia di andarci*: _{desire_to_visit}/10_  "
    
    def render_going(self, params):
        return f"### Andata: **{params.departure_date}** - _{params.price_outward_journey}€_\n\tPartenza: {params.departure_airport_outward_journey} - {params.departure_time_outward_journey}\n\tArrivo: {params.arrival_airport_outward_journey} - {params.arrival_time_outward_journey}"
    
    def render_return(self, params):
        return f"### Ritorno: **{params.return_date}** - _{params.price_return_journey}€_\n\tPartenza: {params.departure_airport_return_journey} - {params.departure_time_return_journey}\n\tArrivo: {params.arrival_airport_return_journey} - {params.arrival_time_return_journey}"

    def render_destination(self, params):
        return f"# {params.destination}"

    def render_ppl_quantity(self, params):
        return f"*Numero Persone*: _{params.number_of_people}_  "

    def render_nights_quantity(self,params):
        return f"*Numero Notti*: _{params.number_of_nights}_  "

    def generate_content(self, params):

        # this is made to not write a f string and indent it all to the left.
        # dedent doesn't work in this case.
        lines =  [
            self.render_destination(params),
            self.render_desire(params),
            self.render_ppl_quantity(params),
            self.render_nights_quantity(params),
            self.render_going(params),
            self.render_return(params),
            self.render_baggage(params),
            self.render_avg_night_cost(params),
            self.render_car_rental(params),
            self.render_home_airport(params),
            self.render_totals(params),
            self.render_notes(params)
        ]

        content = ""
        for line in lines:
            content += str(line) + "  \n"
        
        return content


def main():
    root = tk.Tk()
    app = TravelReportGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
