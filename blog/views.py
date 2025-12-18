from django.shortcuts import render
from datetime import date
from django.http import Http404

# Create your views here.
blog_introduction = "Hi, I am Renjana and I love to blog about Disney movies and series."

all_posts = [
    {
        "title": "Frozen",
        "image": "frozen.jpeg",
        "favourite": True,
        "slug_name": "frozen-movie",
        "directed_by": "Chris Buck, Jennifer Lee",
        "release_date": date(2013,11,27),
        "summary": "Two sisters discover the meaning of love while facing magical chaos.",
        "content": (
            "Princesses Elsa and Anna grow up in the kingdom of Arendelle. Elsa is born with magical ice powers, "
            "but after accidentally injuring Anna as a child, she learns to hide her abilities out of fear. "
            "The sisters grow distant as Elsa isolates herself.\n\n"
            "When Elsa is crowned queen, her powers are revealed during an emotional moment, causing eternal winter "
            "to fall over Arendelle. Elsa flees into the mountains, where she builds an ice palace and embraces her identity.\n\n"
            "Anna sets out to find Elsa and teams up with Kristoff, his reindeer Sven, and Olaf, a cheerful snowman "
            "created by Elsa’s magic. Along the journey, Anna learns that true love is not always romantic.\n\n"
            "In the end, Anna sacrifices herself to save Elsa, proving that an act of true love can thaw a frozen heart. "
            "Elsa gains control of her powers, the winter ends, and the sisters rebuild their bond."
        )
    },
    {
        "title": "Moana",
        "image": "moana.jpeg",
        "favourite": False,
        "slug_name": "moana-movie",
        "directed_by": "Ron Clements, John Musker",
        "release_date": date(2016,11,23),
        "summary": "A young navigator sets sail to save her island with the help of a demigod.",
        "content": (
            "Moana is the daughter of the chief of Motunui, a peaceful island whose people have abandoned voyaging. "
            "When the island’s crops fail and fish disappear, Moana learns the land is dying due to a curse.\n\n"
            "Chosen by the ocean, Moana sets sail to find Maui, a demigod who stole the heart of the goddess Te Fiti. "
            "Together, they face monsters, storms, and Maui’s own self-doubt.\n\n"
            "Moana discovers her identity as a wayfinder and realizes that Te Fiti has become the destructive lava monster Te Kā. "
            "Instead of fighting, Moana restores Te Fiti’s heart with compassion.\n\n"
            "The world is healed, Maui regains his confidence, and Moana returns home to lead her people back to the sea."
        )
    },
    {
        "title": "Cinderella",
        "image": "cinderella.jpeg",
        "favourite": True,
        "slug_name": "cinderella-movie",
        "directed_by": "Clyde Geronimi, Wilfred Jackson, Hamilton Luske",
        "release_date": date(1950,2,15),
        "summary": "A kind-hearted girl overcomes adversity with the help of her fairy godmother.",
        "content": (
            "Cinderella lives a happy life until her father dies, leaving her in the care of her cruel stepmother and jealous stepsisters. "
            "She is forced into servitude but remains kind and hopeful.\n\n"
            "When the king hosts a royal ball to find a bride for the prince, Cinderella is forbidden from attending. "
            "Her Fairy Godmother magically transforms her rags into a beautiful gown and sends her to the ball, "
            "with a warning to return before midnight.\n\n"
            "Cinderella and the Prince fall in love, but she flees as the clock strikes twelve, leaving behind a glass slipper.\n\n"
            "After searching the kingdom, the Prince finds Cinderella. The slipper fits, her true identity is revealed, "
            "and she escapes her hardships to live happily ever after."
        )
    },
    {
        "title": "Beauty and the Beast",
        "image": "beauty_beast.jpeg",
        "favourite": True,
        "slug_name": "beauty-beast-movie",
        "directed_by": "Gary Trousdale, Kirk Wise",
        "release_date": date(1991,11,22),
        "summary": "A young woman learns to love a prince trapped in a beastly form.",
        "content": (
            "A selfish prince is cursed by an enchantress and transformed into a beast, along with his servants, "
            "until he learns to love and be loved in return.\n\n"
            "Belle, a bright and independent young woman, takes her father’s place as the Beast’s prisoner. "
            "Over time, Belle sees beyond the Beast’s appearance and discovers his kindness.\n\n"
            "As their bond grows, the Beast learns selflessness and Belle learns compassion. "
            "Meanwhile, Gaston plots to kill the Beast out of jealousy.\n\n"
            "Belle’s love breaks the curse just in time, restoring the prince and his castle. "
            "Love, kindness, and inner beauty triumph."
        )
    },
    {
        "title": "Aladdin",
        "image": "aladdin.jpeg",
        "favourite": False,
        "slug_name": "aladdin-movie",
        "directed_by": "Ron Clements, John Musker",
        "release_date": date(1992,11,25),
        "summary": "A street-smart boy discovers a magical lamp and a genie who changes his life.",
        "content": (
            "Aladdin is a poor but clever young man living in Agrabah. He meets Princess Jasmine, who longs for freedom "
            "from royal expectations.\n\n"
            "After discovering a magical lamp, Aladdin releases the Genie, who grants him three wishes. "
            "Aladdin wishes to become a prince to win Jasmine’s heart.\n\n"
            "Meanwhile, the villain Jafar seeks the lamp to gain ultimate power. "
            "Through courage and honesty, Aladdin defeats Jafar.\n\n"
            "Aladdin frees the Genie, proving his selflessness. Jasmine chooses Aladdin for who he truly is, "
            "not his status."
        )
    },
    {
        "title": "The Lion King",
        "image": "lion_king.jpeg",
        "favourite": False,
        "slug_name": "the-lion-king-movie",
        "directed_by": "Roger Allers, Rob Minkoff",
        "release_date": date(1994,6,24),
        "summary": "A young lion prince overcomes tragedy to claim his rightful place as king.",
        "content": (
            "Simba is born as the son of King Mufasa and is destined to rule the Pride Lands. "
            "His uncle Scar, jealous of the throne, plots to seize power.\n\n"
            "Scar tricks Simba into believing he caused Mufasa’s death, forcing Simba into exile. "
            "Simba grows up carefree but haunted by guilt.\n\n"
            "With the help of Nala, Rafiki, and the spirit of his father, Simba accepts his responsibility.\n\n"
            "He returns to defeat Scar, restore balance, and take his rightful place as king."
        )
    },
    {
        "title": "Tangled",
        "image": "tangled.jpeg",
        "favourite": False,
        "slug_name": "tangled-movie",
        "directed_by": "Nathan Greno, Byron Howard",
        "release_date": date(2010,11,24),
        "summary": "A spirited princess with magical hair discovers the world beyond her tower.",
        "content": (
            "Rapunzel is a princess kidnapped as a baby by Mother Gothel, who uses Rapunzel’s magical hair to stay young. "
            "Rapunzel grows up isolated in a tower, dreaming of seeing floating lanterns.\n\n"
            "When thief Flynn Rider stumbles into her tower, Rapunzel escapes to explore the world. "
            "Their journey leads to adventure, danger, and self-discovery.\n\n"
            "Rapunzel learns her true identity and confronts Gothel. Flynn sacrifices himself for her, "
            "breaking the magic.\n\n"
            "Rapunzel reunites with her parents and chooses a life of freedom, love, and purpose."
        )
    }
]

def blog_home(request):
    try:
        # Get favourite posts, up to 3
        posts = [post for post in all_posts if post.get('favourite') == True][:3]

        if not posts:
            # Optional: show empty page message
            return render(request, 'blog/blog_home.html', {
                "blog_introduction": blog_introduction,
                "posts": [],
                "message": "No favourite posts available."
            })

        return render(request, 'blog/blog_home.html', {
            "blog_introduction": blog_introduction,
            "posts": posts
        })
    except Exception as e:
        # Log the error if needed
        raise Exception(f"Error loading blog home: {e}")


def collected_post(request):
    try:
        if all_posts:
            return render(request, 'blog/collected_post.html', {"posts": all_posts})
        else:
            # Safe fallback for empty posts
            return render(request, 'blog/collected_post.html', {
                "posts": [],
                "message": "No posts available yet."
            })
    except Exception as e:
        raise Exception(f"Error loading collected posts: {e}")


def individual_post(request, slug):
    try:
        # Safe lookup for a post by slug
        identified_post = next((post for post in all_posts if post.get('slug_name') == slug), None)

        if not identified_post:
            raise Http404("Post not found")

        return render(request, 'blog/single_post.html', {"single_post": identified_post})
    except Http404:
        raise Http404("Post not found")
    except Exception as e:
        raise Exception(f"Error loading individual post: {e}")