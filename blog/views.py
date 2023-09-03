from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "Go-to-the-beach",
        "image": "beach.png",
        "author": "By Aline",
        "date": date(2023, 8, 28),
        "title": "Gigi Islands",
        "excerpt": " There's nothing like the views you get when you go to the beach!",
        "content": """ GiLi Islands, a group of tiny Indonesian Islands for relaxed and laid-back vibe, 
        made me fall so much in love with the destination and myself, that I crave to go back to them over
        and over again. Gili Islands are exotic, quiet, non-polluted, yet, cheap islands for backpackers as
        well as honeymooners.
        """
    },
    {
        "slug": "Beautiful-beach",
        "image": "jurere.png",
        "author": "By Aline",
        "date": date(2021, 7, 15),
        "title": "Jurerê Beach",
        "excerpt": " The beach is very beautiful!",
        "content": """ Jurerê, a group of tiny Indonesian Islands for relaxed and laid-back vibe, 
        made me fall so much in love with the destination and myself, that I crave to go back to them over
        and over again. Gili Islands are exotic, quiet, non-polluted, yet, cheap islands for backpackers as
        well as honeymooners.
        """
    },
    {
        "slug": "Natural-beach",
        "image": "bombinhas.png",
        "author": "By Aline",
        "date": date(2022, 6, 15),
        "title": "Bombinhas Beach",
        "excerpt": " A most famous beach on the south!",
        "content": """ Bombinhas, a group of tiny Indonesian Islands for relaxed and laid-back vibe, 
        made me fall so much in love with the destination and myself, that I crave to go back to them over
        and over again. Gili Islands are exotic, quiet, non-polluted, yet, cheap islands for backpackers as
        well as honeymooners.
        """
    },
     {
        "slug": "Python-Django",
        "image": "python.jpg",
        "author": "By Aline",
        "date": date(2023, 7, 19),
        "title": "Python-Django",
        "excerpt": " See all we can do with Python-Django",
        "content": """ Learn how to build web applications and websites with Python and the Django framework.
        Python is the most popular programming language of the world - it's versatile, easy to learn and very powerful!
        We already got a Python course which you can take if you want to learn Python.
        But one of the primary things you can build with Python is a website! You can use Python for web development.
        And to make that easier, you would typically use a framework like Django - simply because that allows you to 
        focus on your core business logic and you don't need to re-invent the wheel and implement all the nitty-gritty 
        technical details from scratch.
        Django covers all aspects of web development - from handling requests and responses, over rendering dynamic HTML 
        pages with templates, all the way up to making database access and data management easy. It's all baked in and 
        This course teaches Django from the ground up - you don't need to know anything about it to get started. 
        Basic Python and web development knowledge is all you need.
        """
    },
     {
        "slug": "Web-development",
        "image": "web.jpg",
        "author": "By Aline",
        "date": date(2022, 12, 29),
        "title": "Web development",
        "excerpt": " Web development is the work involved in developing a website for the Internet!",
        "content": """ Web development refers to the creating, building, and maintaining of websites. 
        It includes aspects such as web design, web publishing, web programming, and database management. 
        It is the creation of an application that works over the internet i.e. websites.
        Web Development can be classified into two ways: 
        Frontend Development - Backend Development.
        Popular Frontend Technologies:
        HTML, CSS, JavaScript, Bootstrap;
        popular Backend Technologies:
        PHP, Java, Python, Node.js;
        """
    }
]

def get_date(post):
    return post["date"]

# Create your views here.
#passo 2



def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })