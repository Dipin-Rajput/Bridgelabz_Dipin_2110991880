# Music Player

class Song:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.next = None
        self.prev = None

class MusicPlayer:

    def __init__(self):
        self.head = None
        self.current = None

    # addsong(): To add songs to the playlist

    def addsong(self, title, author):

        newsong = Song(title, author)

        if(self.head == None):
            self.head = self.current = newsong
            print(f"\n{title} Added to the playlist")
            return
        
        cursong = self.head
        while(cursong.next != None):
            cursong = cursong.next

        cursong.next = newsong
        newsong.prev = cursong
        print(f"\n{title} Added to the playlist")

    # deletesong(): To delete songs form the playlist

    def deletesong(self):

        if(self.head == None):
            print("\nNo song in the playlist, Add song first")
            return
        
        title = input("\nEnter the title of song you want to delete: ").title()
        
        if(self.head.title == title):
            self.head = self.head.next
            self.head.prev = None
            self.current = self.head
        
        prevsong = self.head
        cursong = self.head.next

        while(cursong != None):
            if(cursong.title == title):
                prevsong.next = cursong.next
                cursong.next.prev = prevsong
                print(f"\n{title} removed from playlist, successfully")
                return
            cursong = cursong.next
            prevsong = prevsong.next

        print(f'\nNo song found with this title "{title}", please enter valid name')

    # play(): To play the current song

    def playsong(self):

        if(self.head == None):
            print("\nPlaylist is Empty, Add song first")
            
        else:
            print(f'\nNow playing: "{self.current.title} by {self.current.author}"')

    # nextsong(): To play the next song

    def nextsong(self):

        if(self.head == None):
            print("\nPlaylist is Empty, Add song first")
            return
        
        if(self.current.next == None):
            print("\nThis is the last song in the playlist")
        else:
            self.current = self.current.next
            self.playsong()

    # prevsong(): To play the prev song

    def prevsong(self):

        if(self.head == None):
            print("\nPlaylist is Empty, Add song first")
            return
        
        if(self.current.prev == None):
            print("\nThis is the first song in the playlist")
        else:
            self.current = self.current.prev
            self.playsong()

    # showplaylist(): To view the songs in the playlist

    def showplaylist(self):

        if(self.head == None):
            print("\nPlaylist is Empty, Add song first")
            return

        cursong = self.head

        print()
        while(cursong != None):
            print(f"{cursong.title} by {cursong.author}")
            cursong = cursong.next

# ---------------------------------------------------------------------------------------------------------------------------------------

player = MusicPlayer()

print("\nPlease select the below options to create your playlist and play the songs")

while True:

    print("\nEnter 1 to add song")
    print("Enter 2 to remove song")
    print("Enter 3 to create playlist from existing songs")
    print("Enter 4 to play songs")
    print("Enter 5 to play next song")
    print("Enter 6 to play prev song")
    print("Enter 7 to play songs form the beginning")
    print("Enter 8 to view playlist")
    print("Press Enter to close the music player")

    choice = input("\nEnter your choice: ")

    match choice:

        case "1":
            title = input("\nEnter song name: ").title()
            author = input("Enter author name: ").title()
            player.addsong(title, author)

        case "2":
            player.deletesong()

        case "3":
            player.addsong("Shape Of You", "Ed Sheeran")
            player.addsong("Bohemian Rhapsody", "Queen")
            player.addsong("Blinding Lights", "The Weeknd")
            player.addsong("Hotel California", "Eagles")
            player.addsong("Rolling In The Deep", "Adele")

        case "4":
            player.playsong()

        case "5":
            player.nextsong()

        case "6":
            player.prevsong()

        case "7":
            player.current = player.head
            player.playsong()

        case "8":
            player.showplaylist()

        case _:
            print("\n------ Closing Music Player ------")
            break