DELETE FROM users;
INSERT INTO users (username, first_name, middle_name, last_name, email, password_hash)
VALUES
('ivanov92', 'Игорь', 'Иванович', 'Иванов', 'ivanov92@medpoisk.ru', bytea '\x243262243132243478667766574676536a474e734f75556f525250654f55575558355276306e4b4d6d792e494b317359303139547870516464654657'),
('petrovna_rus', 'Ольга', 'Михайловна', 'Петровна', 'petrovna_rus@medpoisk.ru', bytea '\x24326224313224317875797476346d7530787076395a617842456d4f6530776a72726f3547727654734251593353786f793339617452306b77467443'),
('sergei_1985',  'Сергей', 'Петрович', 'Сидоров', 'sergei_1985@medpoisk.ru', bytea '\x243262243132246367757777643855645177427164466945675371672e30754b72762f5a533347734b46336e46444f45424170552e6e7944366c2e57'),
('anna_kovaleva',  'Анна', 'Сергеевна', 'Петрова', 'anna_kovaleva@medpoisk.ru', bytea '\x24326224313224736862423461354772584c777764754a54677635754f703353656b6e34515332514d473945474d466c7264416d69415a5442354b43'),
('roman_smirnov',  'Роман', 'Евгениевич', 'Смирнов', 'roman_smirnov@medpoisk.ru', bytea '\x243262243132242e652e3249505131784c56414f2f6c74386b38385a2e6771675a557847554d552e414b78516d484b704a4d594b2f34396c4f534d2e');

DELETE FROM divisions;
INSERT INTO divisions (title, address, super_division_id)
VALUES
('Главный офис', 'ул. Академика Комарова, 14А', NULL);
INSERT INTO divisions (title, address, super_division_id)
VALUES
('Филиал №1', 'Новофилёвский пр., 9', (SELECT id FROM divisions WHERE title='Главный офис')),
('Филиал №2', 'пер. Докучаев, 13', (SELECT id FROM divisions WHERE title='Главный офис'));
INSERT INTO divisions (title, address, super_division_id)
VALUES
('Субфилиал №1', 'пер. Докучаев, 13', (SELECT id FROM divisions WHERE title='Филиал №1'));

DELETE FROM privilages;
INSERT INTO privilages (user_id, division_id, role_name)
VALUES
((SELECT id FROM users WHERE username = 'ivanov92'), (SELECT id FROM divisions WHERE title = 'Главный офис'), 'director'),
((SELECT id FROM users WHERE username = 'petrovna_rus'), (SELECT id FROM divisions WHERE title = 'Филиал №1'), 'manager'),
((SELECT id FROM users WHERE username = 'sergei_1985'), (SELECT id FROM divisions WHERE title = 'Филиал №2'), 'manager'),
((SELECT id FROM users WHERE username = 'anna_kovaleva'), (SELECT id FROM divisions WHERE title = 'Филиал №1'), 'doctor'),
((SELECT id FROM users WHERE username = 'roman_smirnov'), (SELECT id FROM divisions WHERE title = 'Филиал №2'), 'doctor');

DELETE FROM rooms;
INSERT INTO rooms (title, division_id)
VALUES
('Комната №1', (SELECT id FROM divisions WHERE title = 'Главный офис')),
('Комната №2', (SELECT id FROM divisions WHERE title = 'Главный офис')),
('Комната №3', (SELECT id FROM divisions WHERE title = 'Главный офис')),
('Кабинет №1', (SELECT id FROM divisions WHERE title = 'Филиал №1')),
('Кабинет №2', (SELECT id FROM divisions WHERE title = 'Филиал №1')),
('Кабинет №1', (SELECT id FROM divisions WHERE title = 'Филиал №2')),
('Кабинет №2', (SELECT id FROM divisions WHERE title = 'Филиал №2')),
('Кабинет №1', (SELECT id FROM divisions WHERE title = 'Субфилиал №1')),
('Кабинет №2', (SELECT id FROM divisions WHERE title = 'Субфилиал №1'));
