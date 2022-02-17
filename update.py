inputs = ['bouldering', 'rock_climbing']

def write_html(filename, lines):
    def format_row(tag, line):
        return f"<tr align='center'>{''.join([f'<{tag}>{part.strip()}</{tag}>' for part in line])}</tr>"

    with open(f'{filename}.html', 'w') as f:
        header = format_row("th", lines[0])
        rows = '\n'.join(format_row('td', line) for line in lines[1:])
        f.write(f"""<table>
{header}
{rows}
</table>""")

def write_sql(filename, lines):
    pass
 
def update_file(filename):
    with open(f'{filename}.csv') as f:
        lines = [line.split(',') for line in f.readlines()]

        write_html(filename, lines)
        write_sql(filename, lines)

if __name__ == '__main__':
    for filename in inputs:
        update_file(filename)
