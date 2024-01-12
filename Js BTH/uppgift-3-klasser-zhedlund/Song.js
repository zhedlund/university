class Song {
    constructor(id, title, artist) {
        this.id = id;
        this.title = title;
        this.playCount = 0;
        this.artist = artist;
    }

    // Printar låten som spelas och räknar antalet spelningar
    play() {
        console.log(`Playing song: ${this.title} - ${this.artist.name}`); // this.artist.name hämtar namnet på artisten
        this.playCount++;
    }

    // Hämtar antalet spelningar
    getPlayCount() {
        return this.playCount;
    }

    // Visar låttitel och antalet spelningar
    displayInfo() {
        console.log(`Song: ${this.title}`);
        console.log(`Play count: ${this.playCount}`);
    }
}

module.exports = Song;