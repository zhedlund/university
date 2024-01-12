class Album {
    constructor(id, title, artist, genre) {
        this.id = id;
        this.title = title;
        this.artist = artist;
        this.genre = genre;
        this.songs = []; // Array med alla låtar i albumet
    }

    // Visa information om albumet, inkl genre och låtar
    displayInfo() {
        console.log(`\nAlbum: ${this.title}`);
        console.log(`Artist: ${this.artist.name}`);
        this.genre.displayInfo(); // Hämtar info från Genre.js
        console.log("Songs:");
        this.songs.forEach(song => {
            song.displayInfo(); // Hämtar info från Song.js
        });
    }

    // Adderar låt till albumet
    addSong(song) {
        this.songs.push(song);
    }
}

module.exports = Album;