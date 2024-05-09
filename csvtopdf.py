def csv_to_pdf():
    csv_file= 'nutrients_csvfile.csv'
    html_file = csv_file[:-3]+'html'
    
    df = pd.read_csv(csv_file, sep=',') 
    df.to_html(html_file) 
    
    # INSTALL wkhtmltopdf AND SET PATH IN CONFIGURATION 
    # These two Steps could be eliminated By Installing wkhtmltopdf - 
    # - and setting it's path to Environment Variables 
    path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf) 
    
    # CONVERT HTML FILE TO PDF WITH PDFKIT 
    pdfkit.from_url("nutrients_csvfile.html", "FinalOutput.pdf", configuration=config)
