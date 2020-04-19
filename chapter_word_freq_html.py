BEGINNING = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    """

HEAD_END = """
    <!-- The CSS in this style tag is from https://www.w3schools.com/html/html_tables.asp -->
    <style>
        table,
        th,
        td {
            border: 1px solid black;
        }

        th,
        td {
            padding: 15px;
        }
    </style>

</head>

<body>
    <!-- Sorting uses the following script, as explained at
    https://stackoverflow.com/questions/10683712/html-table-sort/51648529 -->
    <script src="https://www.kryogenix.org/code/browser/sorttable/sorttable.js"></script>

    <!-- Inititial table generated using http://convertcsv.com/csv-to-html.htm -->

    <!-- I removed the Bootstrap classes from the generated table. -->
    <!-- <table class="table table-bordered table-hover table-condensed"> -->
    <table class="sortable">
        <thead>
            <tr>
                <th title="Field #1">word</th>
                <th title="Field #2">numInChap</th>
                <th title="Field #3">numInKjv</th>
                <th title="Field #4">weightedRelFreq</th>
                <th title="Field #4">simpleRelFreq</th>
            </tr>
        </thead>
        <tbody>
"""

ENDING = """        </tbody>
    </table>
</body>

</html>
"""


def write_table_row(
    write_file, word, numInChap, numInKjv, weightedRelFreq, simpleRelFreq
):
    write_file.write("            <tr>")
    write_file.write(f"                <td>{word}</td>")
    write_file.write(f"                <td align='right'>{numInChap}</td>")
    write_file.write(f"                <td align='right'>{numInKjv}</td>")
    write_file.write(f"                <td>{weightedRelFreq}</td>")
    write_file.write(f"                <td>{simpleRelFreq}</td>")
    write_file.write("            </tr>")


def write_html_file(words_in_bible, key, html_fn, relative_word_frequency):

    with open(html_fn, "w") as write_file:

        write_file.write(BEGINNING)
        write_file.write(f"<title>{key} - Word Frequencies</title>")
        write_file.write(f"<h1>{key} - Word Frequencies</h1>")
        write_file.write(f"<h2>TOTAL (Gen 1),797,{words_in_bible}</h2>")
        write_file.write(HEAD_END)

        for count, chapter_word_freq in enumerate(relative_word_frequency):
            values = relative_word_frequency[chapter_word_freq]
            if count:  # Data row
                write_table_row(
                    write_file,
                    chapter_word_freq,
                    values[0],
                    values[1],
                    values[2],
                    values[3],
                )

        write_file.write(ENDING)


def main():
    pass


if __name__ == "__main__":
    main()
