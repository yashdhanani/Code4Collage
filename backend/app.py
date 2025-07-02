# ===========================================
# Developed by: Yash Dhanani
# GitHub: github.com/yashdhanani
# ===========================================

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- DATA SOURCE ---
# This dictionary acts as our database.
# Added a 'language' key to each tutorial for the frontend to use.

TUTORIAL_INDEX = [
    {'id': 'html', 'title': 'HTML'}, {'id': 'css', 'title': 'CSS'}, {'id': 'javascript', 'title': 'JAVASCRIPT'},
    {'id': 'sql', 'title': 'SQL'}, {'id': 'python', 'title': 'PYTHON'}, {'id': 'java', 'title': 'JAVA'},
    {'id': 'php', 'title': 'PHP'}, {'id': 'c', 'title': 'C'}, {'id': 'c-plus-plus', 'title': 'C++'},
    {'id': 'c-sharp', 'title': 'C#'}, {'id': 'bootstrap', 'title': 'BOOTSTRAP'}, {'id': 'react', 'title': 'REACT'},
    {'id': 'mysql', 'title': 'MYSQL'}, {'id': 'jquery', 'title': 'JQUERY'}, {'id': 'excel', 'title': 'EXCEL'},
    {'id': 'xml', 'title': 'XML'}, {'id': 'django', 'title': 'DJANGO'}, {'id': 'numpy', 'title': 'NUMPY'},
    {'id': 'pandas', 'title': 'PANDAS'}, {'id': 'nodejs', 'title': 'NODEJS'}, {'id': 'dsa', 'title': 'DSA'},
    {'id': 'typescript', 'title': 'TYPESCRIPT'}, {'id': 'angular', 'title': 'ANGULAR'}, {'id': 'git', 'title': 'GIT'},
    {'id': 'postgresql', 'title': 'POSTGRESQL'}, {'id': 'mongodb', 'title': 'MONGODB'}, {'id': 'asp', 'title': 'ASP'},
    {'id': 'ai', 'title': 'AI'}, {'id': 'r', 'title': 'R'}, {'id': 'go', 'title': 'GO'},
    {'id': 'kotlin', 'title': 'KOTLIN'}, {'id': 'sass', 'title': 'SASS'}, {'id': 'vue', 'title': 'VUE'},
    {'id': 'gen-ai', 'title': 'GEN AI'}, {'id': 'scipy', 'title': 'SCIPY'}, {'id': 'cybersecurity', 'title': 'CYBERSECURITY'},
    {'id': 'data-science', 'title': 'DATA SCIENCE'}, {'id': 'intro-to-programming', 'title': 'INTRO TO PROGRAMMING'},
    {'id': 'bash', 'title': 'BASH'}, {'id': 'rust', 'title': 'RUST'}
]

TUTORIAL_DATABASE = {
    'html': {
        'title': 'HTML Basics', 'language': 'html',
        'content': '# Welcome to HTML!\n\nHTML (HyperText Markup Language) is the standard markup language for documents designed to be displayed in a web browser. It forms the very structure of web pages.',
        'code': '<!DOCTYPE html>\n<html>\n<head>\n    <title>My Page</title>\n</head>\n<body>\n\n    <h1>Welcome to Code4Collage</h1>\n    <p>This is an interactive editor.</p>\n\n</body>\n</html>'
    },
    'css': {
        'title': 'Introduction to CSS', 'language': 'html',
        'content': '# Introduction to CSS\n\nCSS (Cascading Style Sheets) is used to style and lay out web pages — for example, to alter the font, color, size, and spacing of your content. It makes the web look good.',
        'code': '<html>\n<head>\n<style>\nbody {\n  background-color: #f0f8ff;\n  font-family: sans-serif;\n}\n\nh1 {\n  color: #005A9C;\n  text-align: center;\n}\n</style>\n</head>\n<body>\n<h1>Styled Page</h1><p>This is a styled paragraph.</p>\n</body>\n</html>'
    },
    'javascript': {
        'title': 'Introduction to JavaScript', 'language': 'html',
        'content': '# Introduction to JavaScript\n\nJavaScript is a programming language that enables interactive web pages. It is an essential part of web applications, from simple animations to complex frameworks like React and Vue.',
        'code': '<html>\n<body>\n<h2>My First JavaScript</h2>\n<button type="button" onclick="document.getElementById(\'demo\').innerHTML = Date()">Click me to display Date and Time.</button>\n<p id="demo"></p>\n</body>\n</html>'
    },
    'sql': {
        'title': 'Introduction to SQL', 'language': 'sql',
        'content': '# Introduction to SQL\n\nSQL (Structured Query Language) is a standard language for managing and manipulating data in relational databases. You use it to query, insert, update, and delete data.',
        'code': 'SELECT Name, Country FROM Customers\nWHERE Country = \'Canada\';'
    },
    'python': {
        'title': 'Introduction to Python', 'language': 'python',
        'content': '# Introduction to Python\n\nPython is a high-level, general-purpose programming language known for its simple, readable syntax. It\'s widely used in web development, data science, AI, and automation.',
        'code': 'name = "World"\nprint(f"Hello, {name}!")'
    },
    'java': {
        'title': 'Introduction to Java', 'language': 'java',
        'content': '# Introduction to Java\n\nJava is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It\'s a robust language used for large-scale enterprise applications, Android development, and more.',
        'code': 'public class Main {\n  public static void main(String[] args) {\n    System.out.println("Hello, World!");\n  }\n}'
    },
    'php': {
        'title': 'Introduction to PHP', 'language': 'php',
        'content': '# Introduction to PHP\n\nPHP is a popular general-purpose scripting language that is especially suited to web development. It is fast, flexible, and pragmatic, powering everything from your blog to the most popular websites in the world.',
        'code': '<?php\n  $greeting = "Hello";\n  echo $greeting . ", World!";\n?>'
    },
    'c': {
        'title': 'Introduction to C', 'language': 'c',
        'content': '# Introduction to C\n\nC is a powerful, general-purpose programming language. It is fast, portable and available in all platforms. If you are new to programming, C is a good choice to start your programming journey.',
        'code': '#include <stdio.h>\n\nint main() {\n  printf("Hello, World!");\n  return 0;\n}'
    },
    'c-plus-plus': {
        'title': 'Introduction to C++', 'language': 'cpp',
        'content': '# Introduction to C++\n\nC++ is a cross-platform language that can be used to create high-performance applications. It was developed as an extension of the C language, providing more features like object-oriented programming.',
        'code': '#include <iostream>\n\nint main() {\n  std::cout << "Hello, World!";\n  return 0;\n}'
    },
    'c-sharp': {
        'title': 'Introduction to C#', 'language': 'csharp',
        'content': '# Introduction to C#\n\nC# (C-Sharp) is a modern, object-oriented programming language developed by Microsoft. It is widely used for building Windows applications, web applications, and games using the Unity engine.',
        'code': 'using System;\n\nclass Program {\n  static void Main(string[] args) {\n    Console.WriteLine("Hello, World!");\n  }\n}'
    },
    'bootstrap': {
        'title': 'Introduction to Bootstrap', 'language': 'html',
        'content': '# Introduction to Bootstrap\n\nBootstrap is a popular CSS framework for developing responsive and mobile-first websites. It includes pre-built components like buttons, forms, and navigation bars to speed up development.',
        'code': '<div class="container mt-3">\n  <button type="button" class="btn btn-primary">Primary Button</button>\n</div>'
    },
    'react': {
        'title': 'Introduction to React', 'language': 'javascript',
        'content': '# Introduction to React\n\nReact is a JavaScript library for building user interfaces. It lets you compose complex UIs from small and isolated pieces of code called “components”.',
        'code': 'function Greeting({ name }) {\n  return <h1>Hello, {name}</h1>;\n}\n\n// Renders <h1>Hello, Taylor</h1>\nconst element = <Greeting name="Taylor" />;'
    },
    'mysql': {
        'title': 'Introduction to MySQL', 'language': 'sql',
        'content': '# Introduction to MySQL\n\nMySQL is a widely used open-source relational database management system (RDBMS). It\'s a key part of the LAMP stack (Linux, Apache, MySQL, PHP).',
        'code': 'CREATE TABLE Users (\n    UserID int,\n    LastName varchar(255),\n    FirstName varchar(255)\n);'
    },
    'jquery': {
        'title': 'Introduction to jQuery', 'language': 'javascript',
        'content': '# Introduction to jQuery\n\njQuery is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, and animation much simpler with an easy-to-use API that works across a multitude of browsers.',
        'code': '$(document).ready(function(){\n  $("button").click(function(){\n    $("p").hide();\n  });\n});'
    },
    'excel': {
        'title': 'Introduction to Excel', 'language': 'text',
        'content': '# Introduction to Excel\n\nMicrosoft Excel is a spreadsheet program used to record and analyze numerical and statistical data. It provides multiple features to perform various operations like calculations, pivot tables, graph tools, and more.',
        'code': '// Excel uses formulas, not code like this.\n// A common formula to sum values in cells A1 to A5 is:\n=SUM(A1:A5)'
    },
    'xml': {
        'title': 'Introduction to XML', 'language': 'xml',
        'content': '# Introduction to XML\n\nXML (eXtensible Markup Language) is a markup language designed to store and transport data. It\'s designed to be self-descriptive and is often used for configuration files and data exchange.',
        'code': '<note>\n  <to>Tove</to>\n  <from>Jani</from>\n  <heading>Reminder</heading>\n  <body>Don\'t forget me this weekend!</body>\n</note>'
    },
    'django': {
        'title': 'Introduction to Django', 'language': 'python',
        'content': '# Introduction to Django\n\nDjango is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.',
        'code': '# In views.py\nfrom django.http import HttpResponse\n\ndef hello(request):\n    return HttpResponse("Hello, World!")'
    },
    'numpy': {
        'title': 'Introduction to NumPy', 'language': 'python',
        'content': '# Introduction to NumPy\n\nNumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays.',
        'code': 'import numpy as np\n\narr = np.array([1, 2, 3, 4, 5])\nprint(arr)'
    },
    'pandas': {
        'title': 'Introduction to Pandas', 'language': 'python',
        'content': '# Introduction to Pandas\n\nPandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language. It\'s essential for data science workflows.',
        'code': 'import pandas as pd\n\ndata = {\'Name\': [\'Tom\', \'Nick\'], \'Age\': [20, 21]}\ndf = pd.DataFrame(data)\nprint(df)'
    },
    'nodejs': {
        'title': 'Introduction to Node.js', 'language': 'javascript',
        'content': '# Introduction to Node.js\n\nNode.js is an open-source, cross-platform, back-end JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser. It allows developers to use JavaScript for server-side scripting.',
        'code': 'const http = require(\'http\');\n\nhttp.createServer(function (req, res) {\n  res.writeHead(200, {\'Content-Type\': \'text/html\'});\n  res.end(\'Hello World!\');\n}).listen(8080);'
    },
    'dsa': {
        'title': 'Introduction to DSA', 'language': 'text',
        'content': '# Introduction to Data Structures and Algorithms\n\nData Structures and Algorithms (DSA) are a fundamental part of computer science. Data Structures are used to store and organize data, and Algorithms are used to process that data in an efficient way.',
        'code': '// Bubble Sort Example (Pseudocode)\nprocedure bubbleSort(A : list of sortable items)\n    n = length(A)\n    repeat\n        swapped = false\n        for i = 1 to n-1 inclusive do\n            if A[i-1] > A[i] then\n                swap(A[i-1], A[i])\n                swapped = true\n            end if\n        end for\n        n = n - 1\n    until not swapped\nend procedure'
    },
    'typescript': {
        'title': 'Introduction to TypeScript', 'language': 'typescript',
        'content': '# Introduction to TypeScript\n\nTypeScript is a strongly typed programming language that builds on JavaScript, giving you better tooling at any scale. It adds static types to JavaScript, which helps catch errors early in development.',
        'code': """function greet(name: string): string {\n  return `Hello, ${name}!`;\n}\n\nconsole.log(greet("TypeScript User"));"""
    },
    'angular': {
        'title': 'Introduction to Angular', 'language': 'typescript',
        'content': '# Introduction to Angular\n\nAngular is a platform and framework for building single-page client applications using HTML and TypeScript. It is developed and maintained by Google.',
        'code': '// In app.component.ts\nimport { Component } from \'@angular/core\';\n\n@Component({\n  selector: \'app-root\',\n  template: \'<h1>Hello, {{title}}!</h1>\',\n})\nexport class AppComponent {\n  title = \'Angular\';\n}'
    },
    'git': {
        'title': 'Introduction to Git', 'language': 'bash',
        'content': '# Introduction to Git\n\nGit is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. It allows multiple developers to work on the same project without overwriting each other\'s changes.',
        'code': '# Basic Git commands\ngit init      # Initializes a new Git repository\ngit add .     # Stages all changes\ngit commit -m "Initial commit"'
    },
    'postgresql': {
        'title': 'Introduction to PostgreSQL', 'language': 'sql',
        'content': '# Introduction to PostgreSQL\n\nPostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.',
        'code': 'SELECT version();'
    },
    'mongodb': {
        'title': 'Introduction to MongoDB', 'language': 'javascript',
        'content': '# Introduction to MongoDB\n\nMongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas.',
        'code': '// A sample MongoDB document\n{\n  "name": "John Doe",\n  "age": 30,\n  "email": "john.doe@example.com"\n}'
    },
    'asp': {
        'title': 'Introduction to ASP.NET', 'language': 'csharp',
        'content': '# Introduction to ASP.NET\n\nASP.NET is an open-source, server-side web-application framework designed for web development to produce dynamic web pages. It was developed by Microsoft to allow programmers to build dynamic web sites, applications and services.',
        'code': '// In a Razor Page (.cshtml)\n@page\n\n<h1>Hello, world!</h1>\n<p>The time on the server is @DateTime.Now</p>'
    },
    'ai': {
        'title': 'Introduction to AI', 'language': 'python',
        'content': '# Introduction to Artificial Intelligence\n\nArtificial Intelligence (AI) is the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions. The term may also be applied to any machine that exhibits traits associated with a human mind such as learning and problem-solving.',
        'code': '# AI is a broad field, not a single piece of code.\n# This Python code uses a library for a simple task.\n\nfrom textblob import TextBlob\n\ntext = "AI is fascinating!"\nsentiment = TextBlob(text).sentiment\nprint(sentiment)'
    },
    'r': {
        'title': 'Introduction to R', 'language': 'r',
        'content': '# Introduction to R\n\nR is a programming language and free software environment for statistical computing and graphics supported by the R Foundation for Statistical Computing. The R language is widely used among statisticians and data miners for developing statistical software and data analysis.',
        'code': 'myString <- "Hello, World!"\nprint(myString)'
    },
    'go': {
        'title': 'Introduction to Go', 'language': 'go',
        'content': '# Introduction to Go\n\nGo (or Golang) is a statically typed, compiled programming language designed at Google. It is syntactically similar to C, but with memory safety, garbage collection, structural typing, and CSP-style concurrency.',
        'code': 'package main\n\nimport "fmt"\n\nfunc main() {\n    fmt.Println("Hello, World")\n}'
    },
    'kotlin': {
        'title': 'Introduction to Kotlin', 'language': 'kotlin',
        'content': '# Introduction to Kotlin\n\nKotlin is a cross-platform, statically typed, general-purpose programming language with type inference. Kotlin is designed to interoperate fully with Java, and the JVM version of its standard library depends on the Java Class Library, but type inference allows its syntax to be more concise.',
        'code': 'fun main() {\n    println("Hello, World!")\n}'
    },
    'sass': {
        'title': 'Introduction to Sass', 'language': 'scss',
        'content': '# Introduction to Sass\n\nSass (Syntactically Awesome Style Sheets) is a preprocessor scripting language that is interpreted or compiled into Cascading Style Sheets (CSS). It allows you to use variables, nested rules, mixins, and functions in your CSS.',
        'code': '$primary-color: #333;\n\nbody {\n  color: $primary-color;\n}\n\nnav {\n  ul {\n    margin: 0;\n    padding: 0;\n  }\n}'
    },
    'vue': {
        'title': 'Introduction to Vue.js', 'language': 'html',
        'content': '# Introduction to Vue.js\n\nVue is a progressive framework for building user interfaces. Unlike other monolithic frameworks, Vue is designed from the ground up to be incrementally adoptable. The core library is focused on the view layer only, and is easy to pick up and integrate with other libraries or existing projects.',
        'code': '<div id="app">\n  {{ message }}\n</div>\n\n<script>\n  var app = new Vue({\n    el: \'#app\',\n    data: {\n      message: \'Hello Vue!\'\n    }\n  })\n</script>'
    },
    'gen-ai': {
        'title': 'Introduction to Generative AI', 'language': 'text',
        'content': '# Introduction to Generative AI\n\nGenerative AI refers to a category of artificial intelligence algorithms that generate new content, such as text, images, audio, and video. These models learn patterns from existing data and use that knowledge to create new, original outputs.',
        'code': '# This is a conceptual topic.\n# Example: A prompt for a text-generation model.\n\nPrompt: "Write a short poem about the moon."\n\n# The model would then generate a new poem based on its training.'
    },
    'scipy': {
        'title': 'Introduction to SciPy', 'language': 'python',
        'content': '# Introduction to SciPy\n\nSciPy is a free and open-source Python library used for scientific and technical computing. It contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers and other tasks common in science and engineering.',
        'code': 'from scipy import constants\n\n# The speed of light in meters per second\nprint(constants.c)'
    },
    'cybersecurity': {
        'title': 'Introduction to Cybersecurity', 'language': 'text',
        'content': '# Introduction to Cybersecurity\n\nCybersecurity is the practice of protecting systems, networks, and programs from digital attacks. These cyberattacks are usually aimed at accessing, changing, or destroying sensitive information; extorting money from users; or interrupting normal business processes.',
        'code': '# Cybersecurity is a field of practices, not a single program.\n# A Python example for checking password strength:\n\nimport re\n\ndef check_strength(password):\n    if len(password) < 8:\n        return "Weak"\n    if not re.search("[a-z]", password):\n        return "Weak"\n    # ... more checks\n    return "Strong"'
    },
    'data-science': {
        'title': 'Introduction to Data Science', 'language': 'python',
        'content': '# Introduction to Data Science\n\nData Science is an interdisciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data. It combines domain expertise, programming skills, and knowledge of mathematics and statistics to extract meaningful insights from data.',
        'code': '# A typical data science workflow in Python:\n\nimport pandas as pd\n\n# 1. Load data\ndf = pd.read_csv(\'data.csv\')\n\n# 2. Clean data\ndf.dropna(inplace=True)\n\n# 3. Analyze data\nprint(df.describe())'
    },
    'intro-to-programming': {
        'title': 'Introduction to Programming', 'language': 'text',
        'content': '# Introduction to Programming\n\nProgramming is the process of creating a set of instructions that tell a computer how to perform a task. It involves tasks such as analysis, generating algorithms, profiling algorithms\' accuracy and resource consumption, and the implementation of algorithms in a chosen programming language.',
        'code': '// Pseudocode for a basic program\n\nSTART\n  GET number1 from user\n  GET number2 from user\n  \n  sum = number1 + number2\n  \n  PRINT "The sum is: " + sum\nEND'
    },
    'bash': {
        'title': 'Introduction to Bash', 'language': 'bash',
        'content': '# Introduction to Bash\n\nBash is a command-line interpreter or shell for the GNU operating system. It is the default login shell for most Linux distributions. Bash is a powerful tool for automating tasks and managing files.',
        'code': '#!/bin/bash\n\nNAME="World"\necho "Hello, $NAME!"'
    },
    'rust': {
        'title': 'Introduction to Rust', 'language': 'rust',
        'content': '# Introduction to Rust\n\nRust is a multi-paradigm, general-purpose programming language that emphasizes performance, type safety, and concurrency. It enforces memory safety—meaning that all references point to valid memory—without needing a garbage collector.',
        'code': 'fn main() {\n    println!("Hello, world!");\n}'
    }
}


# --- API ENDPOINTS ---

@app.route('/api/tutorials', methods=['GET'])
def get_tutorials():
    """Returns the list of all tutorial topics."""
    return jsonify(TUTORIAL_INDEX)

@app.route('/api/tutorials/<string:tutorial_id>', methods=['GET'])
def get_tutorial_detail(tutorial_id):
    """Returns the content for a specific tutorial."""
    tutorial = TUTORIAL_DATABASE.get(tutorial_id)
    if tutorial:
        return jsonify(tutorial)
    else:
        return jsonify({'error': 'Tutorial not found'}), 404

# This is the entry point for running the Flask application
if __name__ == '__main__':
    # debug=True will auto-reload the server when you make changes
    app.run(debug=True, port=5000)
