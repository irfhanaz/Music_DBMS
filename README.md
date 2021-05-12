# Music_DBMS

Irfhana Zakir Hussain - RA1811027010100

Srivats Tharanilath - RA1811027010076

## Welcome to our DBMS project!

We created a simple music management system in which the entity sets are artists, albums, and songs and where artists are a FK in albums and albums are a FK in songs.

As per real-life music systems, artists can have a 1 to many relationship with albums and albums can have a 1 to many relationship with songs!

### To run our project:
1. Download the full repository.
2. Go to the directory to which it is stored.
3. In terminal type: 
  - python3 manage.py makemigrations
  - python3 manage.py migrate
  - python3 manage.py runserver


### What Songs are in the Playlist Currently?

By clicking “Songs in Playlist” in the MENU, we can view the existing songs in the database. 

![image](https://user-images.githubusercontent.com/58621950/117929706-bd37bb80-b31a-11eb-8c0f-a35691c1ed66.png)
Let’s try adding a song to the playlist. To do this, we need to click on “Upload New Song” in the MENU. 

### The Uploading of Songs:

As you can see, we use a simple html form to get the information needed by the Song object. 

Since the Song object uses Album as a FK and Album uses Artist as FK, it needs both as well. If the Artist or Album object specified does not exist, it is created in the SQL database first. 

Let’s upload a song!

![image](https://user-images.githubusercontent.com/58621950/117929624-a7c29180-b31a-11eb-9ee6-fa97e84ba371.png)


### Viewing Our Uploaded Song in Our Playlist!

You can see the song we uploaded is added to the playlist!

![image](https://user-images.githubusercontent.com/58621950/117929875-eeb08700-b31a-11eb-8e40-d75e005a554c.png)

Now, it’s time to listen to the song. Click on the “Play” button next to the song of choice to listen to the song.


### Playing your Playlist!

We’re now at the Music Player! Click the triangle play button to listen.

![image](https://user-images.githubusercontent.com/58621950/117929928-fff99380-b31a-11eb-9b23-09cc27ce6806.png)

Great song, right?!

You can also navigate between next and previous songs.

### Now that we’ve seen how this works, let’s take a look at the backend.

As you can see there are three entity sets. The first being Artist.

It’s a simple table that merely contains the artist’s name and id (PK).

![image](https://user-images.githubusercontent.com/58621950/117930202-5535a500-b31b-11eb-9b2f-a751082f3066.png)

Then comes Album. In this the Artist_id is a foreign key and the Album_id is the primary key.

![image](https://user-images.githubusercontent.com/58621950/117930157-4818b600-b31b-11eb-9046-47ea800ad59d.png)

In Song, the foreign key is the album_id and the song_id is the primary key. Other attributes are also included such as the title, the audio file, duration, and cover image.  The Artist name, Album name and title form a natural key for the song.

![image](https://user-images.githubusercontent.com/58621950/117930259-65e61b00-b31b-11eb-809e-7900851ad8ab.png)

If we delete an artist, all of their albums and consequently their songs are deleted!

Let’s delete something and return to the user view of the website. To see if it still exists, let’s try the “Search” in MENU.

Since we deleted it, nothing shows up! Now, let’s try searching for something that is in the database. It shows up and we can play it!

![image](https://user-images.githubusercontent.com/58621950/117930016-1c95cb80-b31b-11eb-83aa-ae1389c2619a.png)

![image](https://user-images.githubusercontent.com/58621950/117930094-359e7c80-b31b-11eb-9d52-49ce0c62dd1c.png)

With that we conclude our demo of our DBMS Project! Thank you :))

