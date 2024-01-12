class Genre {
    constructor(id, name) {
        this.id = id;
        this.name = name;
    }

    // Visar genre
    displayInfo() {
        console.log(`Genre: ${this.name}`);
    }
}

module.exports = Genre;
