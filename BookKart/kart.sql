create database bookkart;
USE bookkart;
create table book_details(
    book_name varchar(50), 
    author varchar(50), 
    genre varchar(20), 
    copies BIGINT,
    PRIMARY KEY (book_id)
    );
insert into book_details (book_id, book_name, author, genre, copies)
VALUES
("Digital Fortress", "Dan Brown", "Fiction", 100);
insert into book_details (book_id, book_name, author, genre, copies)
VALUES
("Deception Point", "Dan Brown", "Fiction", 100);
insert into book_details (book_id, book_name, author, genre, copies)
VALUES
("Three Misrakes Of my life", "Chetan Bhagat", "Fiction", 100);
insert into book_details (book_id, book_name, author, genre, copies)
VALUES
("Digital Fortress", "Dan Brown", "Fiction", 100);
insert into book_details (book_id, book_name, author, genre, copies)
VALUES
("Wings Of Fire", "Abdul Kalam", "Auto Biography", 100);


DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `new_book`(
    IN b_name VARCHAR(20),
    IN b_author VARCHAR(20),
    IN b_genre VARCHAR(20),
    IN b_copies BIGINT
)
BEGIN
    if ( select not exists (select 1 from book_details where book_name = b_name) ) THEN
     
        
        insert into book_details
        (
            book_name,
            author,
            genre,
            copies
        )
        values
        (
            b_name,
            b_author,
            b_genre,
            b_copies
        );
     
    END IF;
END$$
DELIMITER ;