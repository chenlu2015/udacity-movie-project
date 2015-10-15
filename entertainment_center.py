#importing necessary libraries
import media
import fresh_tomatoes


movies = [] #create empty list

#create and add movies to the list created previously
movies.append(media.Movie("Finding Nemo", 
	"A fish looking for another fish.", 
	"http://ecx.images-amazon.com/images/I/51-difUGanL.jpg", 
	"https://www.youtube.com/watch?v=wZdpNglLbt8"))

movies.append(media.Movie("Monsters Inc", 
	"A cute movie where monsters find a human baby.", 
	"http://vignette4.wikia.nocookie.net/pixar/images/6/6c/Monsters-Inc-3D-Poster.jpg/revision/20120912005716", 
	"https://www.youtube.com/watch?v=cvOQeozL4S0"))

movies.append(media.Movie("Mulan", 
	"A girl pretends to be a boy to join the army.", 
	"http://ia.media-imdb.com/images/M/MV5BMTIwNjY4NDU2NF5BMl5BanBnXkFtZTcwMzM0OTUyMQ@@._V1_SX640_SY720_.jpg", 
	"https://www.youtube.com/watch?v=MsAniqGowKE"))

movies.append(media.Movie("Guardians of the Galaxy", 
	"Funny movie where the main character saves the world", 
	"http://news.doddleme.com/wp-content/uploads/2014/06/Guardians-Galaxy-Star-Lord-poster.jpg", 
	"https://www.youtube.com/watch?v=d96cjJhvlMA"))

fresh_tomatoes.open_movies_page(movies) #generate html/css and display page
