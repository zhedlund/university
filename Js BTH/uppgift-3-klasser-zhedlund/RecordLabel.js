class RecordLabel {
    constructor(id, name, headOfficeAddress) {
        this.id = id;
        this.name = name;
        this.headOfficeAddress = headOfficeAddress;
        this.albums = []; // Array för att lagra album
    }

    // Visa information om skivbolaget, inkl utgivna album
    displayInfo() {
        console.log(`Record Label: ${this.name}`);
        console.log(`Head Office Address: ${this.headOfficeAddress}`);
        console.log("\nAlbums:");
        this.albums.forEach(album => {
            album.displayInfo(); // Hämtar info från Album.js
        });
    }
}

module.exports = RecordLabel;