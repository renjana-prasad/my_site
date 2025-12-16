from django.shortcuts import render

# Create your views here.
blog_introduction = "Hi, I am Renjana and I love to blog about Disney movies and series."

posts = [
    {
        "title": "Frozen",
        "image": "frozen.jpeg",
        "summary" : "Two sisters discover the meaning of love while facing magical chaos.",
        "content" : "Frozen redefined the idea of true love in Disney films.\nElsa\’s independence and Anna\’s loyalty shine throughout the story.\nIts songs became instant global hits."
    },
    {
        "title": "Moana",
        "image": "moana.jpeg",
        "summary" : "A young navigator sets sail to save her island with the help of a demigod.",
        "content" : "Moana is a celebration of Polynesian culture and mythology.\nThe film\’s animation and music are vibrant and captivating.\nIt inspires viewers to embrace their identity"
    },
    {
        "title": "Cinderella",
        "image": "cinderella.jpeg",
        "summary" : "A kind-hearted girl overcomes adversity with the help of her fairy godmother.",
        "content" : "Cinderella is a timeless tale of hope and kindness.\nThe film\’s classic animation and memorable songs have enchanted audiences for generations.\nIt teaches the value of inner beauty and resilience."
    }
]

def blog_home(request):
    context = {
        "blog_introduction": blog_introduction,
        "posts": posts
    }
    return render(request, 'blog/blog_home.html', context)