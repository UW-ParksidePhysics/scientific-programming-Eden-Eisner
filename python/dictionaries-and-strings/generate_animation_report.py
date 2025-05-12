def parse_animation_code(code_filename):
    """
    Reads a Python file and returns its contents as a string.

    Args:
        code_filename (str): The path to the file containing the animation code.

    Returns:
        str: The contents of the file as a string.
    """
    with open(code_filename, 'r') as file:
        code = file.read()
    return code


def format_section_header(header_string):
    """
    Formats the section header for the HTML report.

    Args:
        header_string (str): The text of the section header.

    Returns:
        str: The HTML formatted header wrapped in <h1> tags.
    """
    return f"<h1>{header_string}</h1>"


def write_html_report(report_string, report_filename):
    """
    Writes the HTML report to a file.

    Args:
        report_string (str): The HTML content to write.
        report_filename (str): The name of the file to write the HTML content to.
    """
    with open(report_filename, 'w') as file:
        file.write(report_string)


def generate_report():
    """
    Generates the HTML report for the animation exercise.
    """
    # File containing the animation code
    animation_code_filename = 'animation_code.py'

    # Paths to images and the GIF file
    plot_files = ['plot1.png', 'plot2.png', 'plot3.png']
    gif_file = 'animation.gif'

    # Read in the animation code
    animation_code = parse_animation_code(animation_code_filename)

    # Format the HTML sections
    header_intro = format_section_header("Animation Exercise Solution")
    header_code = format_section_header("Program Code")
    header_plots = format_section_header("Plots Showing System Changes Over Time")
    header_gif = format_section_header("Animated GIF of the System")

    # Format the code block for the animation code
    code_block = f"<pre>{animation_code}</pre>"

    # Format the plot images
    plot_images = ""
    for i, plot_file in enumerate(plot_files, 1):
        plot_images += f"<h2>Plot {i}</h2><img src='{plot_file}' alt='Plot {i}'><br>"

    # Format the GIF
    gif_section = f"<h2>Animation GIF</h2><img src='{gif_file}' alt='Animated GIF of the system'><br>"

    # Combine all sections into the final report string
    report_string = (
        f"<!DOCTYPE html>\n<html>\n<head>\n<title>Animation Report</title>\n</head>\n<body>\n"
        f"{header_intro}\n"
        f"{header_code}\n{code_block}\n"
        f"{header_plots}\n{plot_images}\n"
        f"{header_gif}\n{gif_section}\n"
        f"</body>\n</html>"
    )

    # Write the HTML report to a file
    write_html_report(report_string, 'animation_report.html')

    print("Report generated: animation_report.html")


# Generate the report
generate_report()
