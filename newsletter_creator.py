import datetime
from headlines import get_headlines
from sports_results import sports
from finance import finance
from science_tech import science

def headlines_code():
    headlines = get_headlines()

    hlines_code = f"""
            <section class="headlines margin-top">
                <p class="large margin-bottom">Headlines</p>
                <div class="table">
                    <table>
                        <tr>
                            <td>
                                <div class="card">
                                    <img src="{headlines[0][0]}" alt="" class="thumbnail">
                                    <p class="medium bold small-margin-bottom">{headlines[0][1]}</p>
                                    <p class="small margin-bottom">{headlines[0][2]}</p>
                                    <a href="{headlines[0][3]}" class="small">Read More</a>
                                </div>
                            </td>
                            <td>
                                <div class="card">
                                    <img src="{headlines[1][0]}" alt="" class="thumbnail">
                                    <p class="medium bold small-margin-bottom">{headlines[1][1]}</p>
                                    <p class="small margin-bottom">{headlines[1][2]}</p>
                                    <a href="{headlines[1][3]}" class="small">Read More</a>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <td>
                                <div class="card">
                                    <img src="{headlines[2][0]}" alt="" class="thumbnail">
                                    <p class="medium bold small-margin-bottom">{headlines[2][1]}</p>
                                    <p class="small margin-bottom">{headlines[2][2]}</p>
                                    <a href="{headlines[2][3]}" class="small">Read More</a>
                                </div>
                            </td>
                            <td>
                                <div class="card">
                                    <img src="{headlines[3][0]}" alt="" class="thumbnail">
                                    <p class="medium bold small-margin-bottom">{headlines[3][1]}</p>
                                    <p class="small margin-bottom">{headlines[3][2]}</p>
                                    <a href="{headlines[3][3]}" class="small">Read More</a>
                                </div>
                            </td>
                        </tr>
                    </table>
                </div>
            </section>
    """
    return hlines_code

def sports_code():
    soccer, bball, madness = sports()

    sports_code = """
            <section class="sports margin-top">
                <p class="large">Sports Results</p>
                <p class="medium-large margin-top margin-bottom">Soccer (PL, La Liga, UCL)</p>
                <div class="table">
                    <table>
                    

    """

    num = 0
    for match in soccer:
        if num %2 == 0:
                sports_code+= """
                <tr>  
        """
        if match[6] == "Scheduled":
            card = f"""
                                <td>
                                    <div class="sportCard">
                                        <table>
                                            <tr>
                                                <td>
                                                    <div class="team">
                                                        <img src="{match[2]}" alt="" class="logo">
                                                        <p class="small">{match[0]}</p>
                                                    </div>
                                                </td>
                                                <td><p class="medium-large">Scheduled</p></td>
                                                <td>
                                                    <div class="team">
                                                        <img src="{match[3]}" alt="" class="logo">
                                                        <p class="small">{match[1]}</p>
                                                    </div>
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                </td>
            """
            num+=1
            sports_code += card
        elif match[6] != "Scheduled" or match[6] != "In Progress":
            card = f"""
                                <td>
                                    <div class="sportCard">
                                        <table>
                                            <tr>
                                                <td>
                                                    <div class="team">
                                                        <img src="{match[2]}" alt="" class="logo">
                                                        <p class="small">{match[0]}</p>
                                                    </div>
                                                </td>
                                                <td><p class="large">{match[4]}</p></td>
                                                <td><p class="large">-</p></td>
                                                <td><p class="large">{match[5]}</p></td>
                                                <td>
                                                    <div class="team">
                                                        <img src="{match[3]}" alt="" class="logo">
                                                        <p class="small">{match[1]}</p>
                                                    </div>
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                </td>
            """
            num+=1

            sports_code += card

            if num %4 == 0:
                sports_code+= """
                </tr>    
            """
            
    sports_code += """
                </table>
                <br>
                <p class="medium-large margin-top margin-bottom">NBA</p>
                <table>
"""            

    num = 0
    for match in bball:
        if num %2 == 0:
                sports_code+= """
                <tr>  
        """
        if match[6] == "Scheduled":
            card = f"""
                                <td>
                                    <div class="sportCard">
                                        <table>
                                            <tr>
                                                <td>
                                                    <div class="team">
                                                        <img src="{match[2]}" alt="" class="logo">
                                                        <p class="small">{match[0]}</p>
                                                    </div>
                                                </td>
                                                <td><p class="medium-large">Scheduled</p></td>
                                                <td>
                                                    <div class="team">
                                                        <img src="{match[3]}" alt="" class="logo">
                                                        <p class="small">{match[1]}</p>
                                                    </div>
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                </td>
            """
            num+=1
            sports_code += card
        elif match[6] != "In Progress":
            card = f"""
                                <td>
                                    <div class="sportCard">
                                        <table>
                                            <tr>
                                                <td>
                                                    <div class="team">
                                                        <img src="{match[2]}" alt="" class="logo">
                                                        <p class="small">{match[0]}</p>
                                                    </div>
                                                </td>
                                                <td><p class="large">{match[4]}</p></td>
                                                <td><p class="large">-</p></td>
                                                <td><p class="large">{match[5]}</p></td>
                                                <td>
                                                    <div class="team">
                                                        <img src="{match[3]}" alt="" class="logo">
                                                        <p class="small">{match[1]}</p>
                                                    </div>
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                </td>
            """
            num+=1
            sports_code += card

            if num %4 == 0:
                sports_code+= """
                </tr>    
    
        """
    


    sports_code += """
                </table>
                <br>
                <p class="medium-large margin-top margin-bottom">March Madness</p>
                <table>
    """

    num = 0
    for match in madness:
        if num %2 == 0:
                sports_code+= """
                <tr>  
        """
        if match[6] == "Scheduled":
            card = f"""
                                <td>
                                    <div class="sportCard">
                                        <table>
                                            <tr>
                                                <td>
                                                    <div class="team">
                                                        <img src="{match[2]}" alt="" class="logo">
                                                        <p class="small">{match[0]}</p>
                                                    </div>
                                                </td>
                                                <td><p class="medium-large">Scheduled</p></td>
                                                <td>
                                                    <div class="team">
                                                        <img src="{match[3]}" alt="" class="logo">
                                                        <p class="small">{match[1]}</p>
                                                    </div>
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                </td>
            """
            num+=1
            sports_code += card
        elif match[6] != "In Progress":
            card = f"""
                                <td>
                                    <div class="sportCard">
                                        <table>
                                            <tr>
                                                <td>
                                                    <div class="team">
                                                        <img src="{match[2]}" alt="" class="logo">
                                                        <p class="small">{match[0]}</p>
                                                    </div>
                                                </td>
                                                <td><p class="large">{match[4]}</p></td>
                                                <td><p class="large">-</p></td>
                                                <td><p class="large">{match[5]}</p></td>
                                                <td>
                                                    <div class="team">
                                                        <img src="{match[3]}" alt="" class="logo">
                                                        <p class="small">{match[1]}</p>
                                                    </div>
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                </td>
            """
            num+=1

            sports_code += card

            if num %4 == 0:
                sports_code+= """
                </tr>    
        """
    sports_code += """
                    </table>
                </div>
            </section>
    """

    return sports_code

def finance_code():
    fin_res = finance()

    fin_code = f"""
            <section class="finance margin-top">
                <p class="large">Finance</p>
                <table>
                    <tr>
                        <td>
                            <div class="card">
                                <img src="{fin_res[0][0]}" alt="" class="thumbnail">
                                <p class="medium bold small-margin-bottom">{fin_res[0][1]}</p>
                                <p class="small margin-bottom">{fin_res[0][2]}</p>
                                <a href="{fin_res[0][3]}" class="small">Read More</a>
                            </div>
                        </td>
                        <td>
                            <div class="card">
                                <img src="{fin_res[1][0]}" alt="" class="thumbnail">
                                <p class="medium bold small-margin-bottom">{fin_res[1][1]}</p>
                                <p class="small margin-bottom">{fin_res[1][2]}</p>
                                <a href="{fin_res[1][3]}" class="small">Read More</a>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div class="card">
                                <img src="{fin_res[2][0]}" alt="" class="thumbnail">
                                <p class="medium bold small-margin-bottom">{fin_res[2][1]}</p>
                                <p class="small margin-bottom">{fin_res[2][2]}</p>
                                <a href="{fin_res[2][3]}" class="small">Read More</a>
                            </div>
                        </td>
                        <td>
                            <div class="card">
                                <img src="{fin_res[3][0]}" alt="" class="thumbnail">
                                <p class="medium bold small-margin-bottom">{fin_res[3][1]}</p>
                                <p class="small margin-bottom">{fin_res[3][2]}</p>
                                <a href="{fin_res[3][3]}" class="small">Read More</a>
                            </div>
                        </td>
                    </tr>
                </table>
            </section>
    """
    return fin_code

def science_code():
     news = science()
     science_code = f"""
            <section class="science margin-top">
                <p class="large">Science/Tech</p>
                <table>
                    <tr>
                        <td>
                            <div class="card">
                                <img src="{news[0][0]}" alt="" class="thumbnail">
                                <p class="medium bold small-margin-bottom">{news[0][1]}</p>
                                <p class="small margin-bottom">{news[0][2]}</p>
                                <a href="{news[0][3]}" class="small">Read More</a>
                            </div>
                        </td>
                        <td>
                            <div class="card">
                                <img src="{news[1][0]}" alt="" class="thumbnail">
                                <p class="medium bold small-margin-bottom">{news[1][1]}</p>
                                <p class="small margin-bottom">{news[1][2]}</p>
                                <a href="{news[1][3]}" class="small">Read More</a>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <div class="card">
                                <img src="{news[2][0]}" alt="" class="thumbnail">
                                <p class="medium bold small-margin-bottom">{news[2][1]}</p>
                                <p class="small margin-bottom">{news[2][2]}</p>
                                <a href="{news[2][3]}" class="small">Read More</a>
                            </div>
                        </td>
                        <td>
                            <div class="card">
                                <img src="{news[3][0]}" alt="" class="thumbnail">
                                <p class="medium bold small-margin-bottom">{news[3][1]}</p>
                                <p class="small margin-bottom">{news[3][2]}</p>
                                <a href="{news[3][3]}" class="small">Read More</a>
                            </div>
                        </td>
                    </tr>
                </table>
            </section>
    """
     return science_code

def footer_code():
     footer = """
            <footer class="footer margin-top">
                <hr>
                <br>
                <p class="small">Copyright © Newsletter 2025, All rights reserved</p>
                <br>
                <p class="small">About <a class="lakshan" href="lakshansuresh.netlify.app">Lakshan Suresh</a></p>
                <br>
                <hr class="margin-bottom">
            </footer>
    """
     return footer

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newsletter</title>
</head>
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Work+Sans:ital,wght@0,100..900;1,100..900&display=swap');
    :root {
        --font1: "DM Sans", sans-serif;
        --font2: "Work Sans", sans-serif;
    }

    * {
        margin: 0;
        padding: 0;
        font-size: 100%;
        vertical-align: baseline;
    }

    article {
        width: 80%;
        margin: auto;
    }

    .large {
        font-family: var(--font1);
        font-size: 35px;
        color: #333;
        font-weight: bold;
    }

    .medium-large {
        font-family: var(--font1);
        font-size: 25px;
    }

    .small {
        font-family: var(--font2);
        color: black;
        font-size: 20px;
    }

    .medium {
        font-family: var(--font2);
        font-size: 25px;
    }

    .littleSpace {
        padding: 20px;
    }

    .mediumSpace {
        padding: 40px;
    }

    .largeSpace {
        padding: 60px;
    }

    .margin-top {
        margin-top: 20px;
    }

    .margin-bottom {
        margin-bottom: 20px;
    }

    .small-margin-top {
        margin-top: 5px;
    }

    .small-margin-bottom {
        margin-bottom: 5px;
    }

    .bold {
        font-weight: bold;
    }

    .card {
        padding: 25px 15px;
        border: 3px solid #333;
        border-radius: 10px;
        width: 400px;
    }

    img {
        width: 100%;
        border-radius: 10px;
    }

    .sports {
        margin-top: 50px;
    }

    a:not(.lakshan) {
        padding: 10px;
        border: 2px solid #333;
        border-radius: 5px;
        color: black;
        text-decoration: none;
    }

    .cardContainer {
        gap: 30px 20px;
    }

    .card img {
        height: 250px;
        object-fit: cover;
    }

    .sportCard {
        height: 130px;
        width: 350px;
        padding: 10px;
        border: 3px solid #333;
        border-radius: 10px;
    }

    .table {
        width: 100%;
    }

    .sportCard table tr td {
        width: 30%;
        padding: 5px;
        text-align: center;
    }

    .headlines table tr td, .sports table tr td {
        padding: 5px;
    }

    .team img {
        margin: 10px;
    }

    .logo {
        width: 50px;
        aspect-ratio: 1 1;
    }

    .footer {
        padding: 20px 0;
    }

    table, caption, tbody, tfoot, thead, tr, th, td  {
    margin: 0;
    padding: 0;
    border: 0;
    outline: 0;
    font-size: 100%;
    vertical-align: baseline;
    background: transparent;
    }

    table {
        text-align: left;
    }
</style>
<body>
    <article>
        <div class="marginTop newsletterContainer">
            <h1 class="large">Newsletter for Today</h1>
            <div class="margin-top">
                <hr>
                <div class="littleSpace  dateContainer">
                    <p class="medium">March 23, 2025</p>
                    <p class="small">Lakshan Suresh</p>
                </div>
                <hr>
            </div>
            
"""
# <div class="margin-top margin-bottom">
#                 <p class="medium">Welcome!<br><br>I publish AI newsletters every morning with curated AI/tech news stories, cool AI projects, and technical research papers. Grab your coffee beans and catch up on yesterday’s top bytes!</p>
#             </div>
#             <hr>

html_code += headlines_code()
html_code += sports_code()
html_code += finance_code()
html_code += science_code()
html_code += footer_code()

html_code += """
    </div>
    </article>
</body>
</html>
"""

html_file = open("generated_newsletter.html", "w")

html_file.write(html_code)