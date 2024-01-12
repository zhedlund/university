class User {
    constructor(id, name) {
        this.id = id;
        this.name = name;
        this.playedSongs = []; // Array för att lagra spelade låtar
    }

    // Spelar en låt och lägger till den i playedSongs
    playSong(song) {
        song.play();
        this.playedSongs.push(song);
    }

    // Visar användarnamn
    displayInfo() {
        console.log(`\nUser: ${this.name}`);
    }

    // Visar låtar som användaren har spelat
    displayPlayedSongs() {
        console.log(`${this.name}'s Played Songs:`);
        this.playedSongs.forEach(song => { 
            console.log(song.title);
        });
    }
}

module.exports = User;