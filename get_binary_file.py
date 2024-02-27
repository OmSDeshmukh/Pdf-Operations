def get_binary_file_downloader_html(file_path, file_content):
    bin_str = file_content.encode('base64').decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_path}">Click here to download</a>'
    return href