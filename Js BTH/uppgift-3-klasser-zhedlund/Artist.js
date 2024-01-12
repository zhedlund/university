class Artist {
    constructor(id, name, genre, bio) {
        this.id = id;
        this.name = name;
        this.genre = genre;
        this.bio = bio;
    }

    // Visa information om artisten
    displayInfo() {
        console.log(`Artist: ${this.name} (${this.genre.name})`); // this.genre.name hämtar namnet på genren
        console.log(`Bio: ${this.bio}`);
    }
}

module.exports = Artist;