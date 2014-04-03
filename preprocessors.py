import re

RE1 = r"terminal:(?P<line>.*)endterminal"


def preprocess(text):
    text = preprocess_terminal(text)
    return text


def preprocess_terminal(text):
    try:
        # Search for terminal blocks.
        m = re.search(RE1, text, re.DOTALL)
        c = [filter(None, match.split("    ")) for match in m.groups('line')]
        t_lines = str()  # The lines or input of the terminal representation.
        for line in c[0]:
            if line[0] == '$':
                t_lines += "<div class='terminal-line'><b>%s</b></div>" % line
            else:
                t_lines += "<div class='terminal-line'>%s</div>" % line
        # Build the final terminal block.
        terminal = """<div class="terminal-container"><div class="terminal-top">
        <div class="terminal-top-text">/bin/bash</div><div class="mock-buttons">
        <div class="terminal-but terminal-but-mini"></div>
        <div class="terminal-but terminal-but-max"></div>
        <div class="terminal-but"></div></div></div><div class="terminal-box">
        %s</div><div class="terminal-bottom"></div></div>""" % t_lines
        # Swap out the markup with the generated code.
        result = text.replace(m.group(), terminal)
        return result
    except AttributeError:
        return text
