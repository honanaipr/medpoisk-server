DELETE FROM employee;
DELETE FROM division;
DELETE FROM privilage;
DELETE FROM room;
DELETE FROM product;
DELETE FROM place;
DELETE FROM inventory;
DELETE FROM minamount;

INSERT INTO employee (username, first_name, middle_name, last_name, email, password_hash)
VALUES
('ivanov92', 'Игорь', 'Иванович', 'Иванов', 'ivanov92@medpoisk.ru', bytea '\x243262243132243478667766574676536a474e734f75556f525250654f55575558355276306e4b4d6d792e494b317359303139547870516464654657'),
('petrovna_rus', 'Ольга', 'Михайловна', 'Петровна', 'petrovna_rus@medpoisk.ru', bytea '\x24326224313224317875797476346d7530787076395a617842456d4f6530776a72726f3547727654734251593353786f793339617452306b77467443'),
('sergei_1985',  'Сергей', 'Петрович', 'Сидоров', 'sergei_1985@medpoisk.ru', bytea '\x243262243132246367757777643855645177427164466945675371672e30754b72762f5a533347734b46336e46444f45424170552e6e7944366c2e57'),
('anna_kovaleva',  'Анна', 'Сергеевна', 'Петрова', 'anna_kovaleva@medpoisk.ru', bytea '\x24326224313224736862423461354772584c777764754a54677635754f703353656b6e34515332514d473945474d466c7264416d69415a5442354b43'),
('roman_smirnov',  'Роман', 'Евгениевич', 'Смирнов', 'roman_smirnov@medpoisk.ru', bytea '\x243262243132242e652e3249505131784c56414f2f6c74386b38385a2e6771675a557847554d552e414b78516d484b704a4d594b2f34396c4f534d2e');


INSERT INTO division (title, address, super_division_id)
VALUES
('Главный офис', 'ул. Академика Комарова, 14А', NULL);
INSERT INTO division (title, address, super_division_id)
VALUES
('Филиал №1', 'Новофилёвский пр., 9', (SELECT id FROM division WHERE title='Главный офис')),
('Филиал №2', 'пер. Докучаев, 13', (SELECT id FROM division WHERE title='Главный офис'));
INSERT INTO division (title, address, super_division_id)
VALUES
('Субфилиал №1', 'пер. Докучаев, 13', (SELECT id FROM division WHERE title='Филиал №1'));


INSERT INTO privilage (employee_id, division_id, role_name)
VALUES
((SELECT id FROM employee WHERE username = 'ivanov92'), (SELECT id FROM division WHERE title = 'Главный офис'), 'director'),
((SELECT id FROM employee WHERE username = 'petrovna_rus'), (SELECT id FROM division WHERE title = 'Филиал №1'), 'manager'),
((SELECT id FROM employee WHERE username = 'sergei_1985'), (SELECT id FROM division WHERE title = 'Филиал №2'), 'manager'),
((SELECT id FROM employee WHERE username = 'anna_kovaleva'), (SELECT id FROM division WHERE title = 'Филиал №1'), 'doctor'),
((SELECT id FROM employee WHERE username = 'roman_smirnov'), (SELECT id FROM division WHERE title = 'Филиал №2'), 'doctor');


INSERT INTO room (title, division_id)
VALUES
('Комната №1', (SELECT id FROM division WHERE title = 'Главный офис')),
('Комната №2', (SELECT id FROM division WHERE title = 'Главный офис')),
('Комната №3', (SELECT id FROM division WHERE title = 'Главный офис')),
('Кабинет №1', (SELECT id FROM division WHERE title = 'Филиал №1')),
('Кабинет №2', (SELECT id FROM division WHERE title = 'Филиал №1')),
('Кабинет №1', (SELECT id FROM division WHERE title = 'Филиал №2')),
('Кабинет №2', (SELECT id FROM division WHERE title = 'Филиал №2')),
('Кабинет №1', (SELECT id FROM division WHERE title = 'Субфилиал №1')),
('Кабинет №2', (SELECT id FROM division WHERE title = 'Субфилиал №1'));


INSERT INTO product (title, description, barcode)
VALUES
('Аспирин', 'Аспирин, также известный как ацетилсалициловая кислота, широко используется как анальгетик, жаропонижающее и противовоспалительное средство. Он помогает снизить боль, устранить лихорадку и уменьшить воспаление.', 8712345678912),
('Парацетамол', 'Парацетамол - это безрецептурное лекарство, которое обычно используется для облегчения боли и жаропонижения. Он помогает справиться с головной болью, зубной болью, мышечными болями и другими неблагоприятными ощущениями.', 5901234567893),
('Ибупрофен', 'Ибупрофен является противовоспалительным, жаропонижающим и анальгетическим препаратом. Он широко используется для облегчения боли, воспаления и жара, таких как головная боль, артрит и ревматизм.', 0123456789012),
('Амоксициллин', 'Амоксициллин - это антибиотик из группы пенициллинов, который используется для лечения различных инфекций, вызванных бактериями. Он может применяться для лечения инфекций дыхательных путей, мочевыводящей системы, кожи и других органов.', 9781234567890),
('Декстра-мед', 'Декстра-мед, или декстрометорфан, является антиитовым препаратом, который используется для облегчения сухого кашля. Он подавляет рефлекс кашля, помогая облегчить частые или непродуктивные приступы кашля.', 1234567890123),
('Лоратадин', 'Лоратадин - это антигистаминное лекарство, которое обычно применяется для снижения симптомов аллергических реакций, таких как заложенность носа, крапивница и зуд. Он помогает справиться с аллергическим ринитом и сезонными аллергиями.', 4567890123456),
('Ранитидин', 'Ранитидин - это препарат, который снижает количество кислоты в желудке и широко используется для лечения таких пищеварительных проблем, как изжога, язва желудка и кислотный рефлюкс.', 9876543210987),
('Витамин С', 'Витамин С (аскорбиновая кислота) является незаменимым питательным веществом для организма. Он помогает поддерживать иммунную систему, улучшает абсорбцию железа и помогает в процессе регенерации тканей.', 6543210987654),
('Инсулин', 'Инсулин - это гормон, производимый поджелудочной железой, который регулирует уровень сахара в крови. Он используется для лечения диабета и помогает контролировать уровни глюкозы в организме.', 3210987654321),
('Пропранолол', 'Пропранолол - это бета-адреноблокатор, используемый для лечения высокого кровяного давления, аритмии и других сердечно-сосудистых проблем. Он помогает снизить частоту сердечных сокращений и контролировать симптомы связанных с сердечными заболеваниями.', 7890123456789);


INSERT INTO place (title, division_id)
VALUES
('Шкаф №1', (SELECT id FROM division WHERE title = 'Филиал №1')),
('Шкаф №2', (SELECT id FROM division WHERE title = 'Филиал №1')),
('Ящик №1', (SELECT id FROM division WHERE title = 'Филиал №1')),
('Ящик №2', (SELECT id FROM division WHERE title = 'Филиал №1')),
('Холодильник', (SELECT id FROM division WHERE title = 'Филиал №1')),
('Морозильник', (SELECT id FROM division WHERE title = 'Филиал №1')),
('Шкаф №1', (SELECT id FROM division WHERE title = 'Филиал №2')),
('Шкаф №2', (SELECT id FROM division WHERE title = 'Филиал №2')),
('Ящик №1', (SELECT id FROM division WHERE title = 'Филиал №2')),
('Ящик №2', (SELECT id FROM division WHERE title = 'Филиал №2')),
('Холодильник', (SELECT id FROM division WHERE title = 'Филиал №2')),
('Морозильник', (SELECT id FROM division WHERE title = 'Филиал №2')),
('Шкаф №1', (SELECT id FROM division WHERE title = 'Субфилиал №1')),
('Шкаф №2', (SELECT id FROM division WHERE title = 'Субфилиал №1')),
('Ящик №1', (SELECT id FROM division WHERE title = 'Субфилиал №1')),
('Ящик №2', (SELECT id FROM division WHERE title = 'Субфилиал №1')),
('Холодильник', (SELECT id FROM division WHERE title = 'Субфилиал №1')),
('Морозильник', (SELECT id FROM division WHERE title = 'Субфилиал №1'));


INSERT INTO inventory (product_id, place_id, amount)
VALUES
((SELECT id FROM product WHERE title = 'Аспирин'), (SELECT id FROM place WHERE title = 'Шкаф №1' AND division_id = (SELECT id FROM division WHERE title='Филиал №1')), 5),
((SELECT id FROM product WHERE title = 'Парацетамол'), (SELECT id FROM place WHERE title = 'Шкаф №2' AND division_id = (SELECT id FROM division WHERE title='Филиал №1')), 5),
((SELECT id FROM product WHERE title = 'Ибупрофен'), (SELECT id FROM place WHERE title = 'Ящик №1' AND division_id = (SELECT id FROM division WHERE title='Филиал №1')), 4),
((SELECT id FROM product WHERE title = 'Амоксициллин'), (SELECT id FROM place WHERE title = 'Ящик №2' AND division_id = (SELECT id FROM division WHERE title='Филиал №1')), 1),
((SELECT id FROM product WHERE title = 'Амоксициллин'), (SELECT id FROM place WHERE title = 'Холодильник' AND division_id = (SELECT id FROM division WHERE title='Филиал №1')), 8),
((SELECT id FROM product WHERE title = 'Декстра-мед'), (SELECT id FROM place WHERE title = 'Морозильник' AND division_id = (SELECT id FROM division WHERE title='Филиал №1')), 2),
((SELECT id FROM product WHERE title = 'Лоратадин'), (SELECT id FROM place WHERE title = 'Шкаф №1' AND division_id = (SELECT id FROM division WHERE title='Филиал №2')), 9),
((SELECT id FROM product WHERE title = 'Ранитидин'), (SELECT id FROM place WHERE title = 'Шкаф №2' AND division_id = (SELECT id FROM division WHERE title='Филиал №2')), 1),
-- ((SELECT id FROM product WHERE title = 'Витамин'), (SELECT id FROM place WHERE title = 'Ящик №1' AND division_id = (SELECT id FROM division WHERE title='Филиал №2')), 7),
((SELECT id FROM product WHERE title = 'Инсулин'), (SELECT id FROM place WHERE title = 'Ящик №2' AND division_id = (SELECT id FROM division WHERE title='Филиал №2')), 3),
((SELECT id FROM product WHERE title = 'Пропранолол'), (SELECT id FROM place WHERE title = 'Холодильник' AND division_id = (SELECT id FROM division WHERE title='Филиал №2')), 6),
((SELECT id FROM product WHERE title = 'Аспирин'), (SELECT id FROM place WHERE title = 'Морозильник' AND division_id = (SELECT id FROM division WHERE title='Филиал №2')), 7);


INSERT INTO minamount (product_id, division_id, min_amount)
VALUES
((SELECT id FROM product WHERE title = 'Аспирин'), (SELECT id FROM division WHERE title = 'Филиал №1'), 1),
((SELECT id FROM product WHERE title = 'Парацетамол'), (SELECT id FROM division WHERE title = 'Филиал №1'), 2),
((SELECT id FROM product WHERE title = 'Ибупрофен'), (SELECT id FROM division WHERE title = 'Филиал №1'), 3),
((SELECT id FROM product WHERE title = 'Амоксициллин'), (SELECT id FROM division WHERE title = 'Филиал №1'), 4);
