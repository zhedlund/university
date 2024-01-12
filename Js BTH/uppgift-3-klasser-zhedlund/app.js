const Artist = require('./Artist');
const Genre = require('./Genre');
const Song = require('./Song');
const Album = require('./Album');
const RecordLabel = require('./RecordLabel');
const User = require('./User');

// Genrer
const downGenre = new Genre(1, 'Downtempo');
const progGenre = new Genre(2, 'Progressive Rock');
const technoGenre = new Genre(3, 'Techno');

// Skivbolag
const recordLabel = new RecordLabel(1, 'Xperimental Music Inc.', '123 Music Street');

// Artister
const artist1 = new Artist(1, 'Riyoon', downGenre, 'Riyoon - meaning \'dream\' in Somalian - is a music producer & DJ. He brings power to those who like it slow, to those who dance into the next day, to those who connect through movement, to those who like rolling basslines, slow beats & shuffled grooves.\n');
const artist2 = new Artist(2, 'Porcupine Tree', progGenre, 'A hugely influential, relentlessly creative British progressive rock band. Sometimes referred to as \'The greatest band you\'ve never heard of\'.\n');
const artist3 = new Artist(3, 'Linn Elisabet', technoGenre, 'Berlin based producer, DJ and singer. Led by their own ethereal vocals, raw broken beats, and immersive sound design. Their contemporary and transgressive interpretation of techno strives to reimagine possibility and desire.\n');

// Album och låtar
const album1 = new Album(1, 'No Mind\'s Land', artist1, downGenre);
const song1 = new Song(1, 'No Mind\'s Land', artist1);
const song2 = new Song(2, 'No Minds Land - okuma Remix', artist1);
const song3 = new Song(3, 'State of Surrender', artist1);
const song4 = new Song(4, 'Temple Boy', artist1);
album1.addSong(song1);
album1.addSong(song2);
album1.addSong(song3);
album1.addSong(song4);

const album2 = new Album(2, 'Voyage 34', artist2, progGenre);
const song5 = new Song(5, 'Phase I', artist2);
const song6 = new Song(6, 'Phase II', artist2);
const song7 = new Song(7, 'Phase III (Astralasia Dreamstate)', artist2);
const song8 = new Song(8, 'Phase IV (A New Civilization)', artist2);
album2.addSong(song5);
album2.addSong(song6);
album2.addSong(song7);
album2.addSong(song8);

const album3 = new Album(3, '47034', artist3, technoGenre);
const song9 = new Song(9, 'In Which I am Reflected', artist3);
const song10 = new Song(10, 'Emotion vs Affect (I Hear Too Much)', artist3);
const song11 = new Song(11, 'Feeding Into Each Other', artist3);
const song12 = new Song(12, 'Challenge Me', artist3);
album3.addSong(song9);
album3.addSong(song10);
album3.addSong(song11);
album3.addSong(song12);

// Lägg till album i skivbolagets lista
recordLabel.albums.push(album1, album2);

// Skapa användare
const user1 = new User(1, 'Sarah');
const user2 = new User(2, 'Billie');
const user3 = new User(3, 'Alex');
const user4 = new User(4, 'Kelly');

// Användare spelar låtar
user1.playSong(song8);
user1.playSong(song9);
user1.playSong(song10);
user1.playSong(song11);
user2.playSong(song5);
user2.playSong(song6);
user2.playSong(song7);
user2.playSong(song8);
user3.playSong(song1);
user3.playSong(song2);
user3.playSong(song3);
user3.playSong(song4);
user4.playSong(song1);
user4.playSong(song5);
user4.playSong(song11);
user4.playSong(song12);

// Visar information om artister
console.log('\n--- Artist Info ---\n');
artist1.displayInfo();
artist2.displayInfo();
artist3.displayInfo();

// Visar information om album
console.log('\n--- Album Info ---');
album1.displayInfo();
album2.displayInfo();
album3.displayInfo();

// Visar information om skivbolaget
console.log('\n--- Record Label Info ---\n');
recordLabel.displayInfo();

// Visa användarnamn och spelade låtar
console.log('\n--- User Info ---');
user1.displayInfo();
user1.displayPlayedSongs();
user2.displayInfo();
user2.displayPlayedSongs();
user3.displayInfo();
user3.displayPlayedSongs();
user4.displayInfo();
user4.displayPlayedSongs();