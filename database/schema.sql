PRAGMA foreign_keys = OFF;


-- Users table with UNIQUE constraints
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER,
    skintype TEXT,
    profile_pic TEXT
);

-- Products table with UNIQUE product_name
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT UNIQUE NOT NULL,
    type TEXT,
    amazon_link TEXT,
    directions TEXT,
    shelflife INTEGER,
    ingredients TEXT,
    product_pic TEXT
    
);

-- Collections table (user_id + product_id should be unique together)
CREATE TABLE IF NOT EXISTS Collections (
    collection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    created_at DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    UNIQUE(user_id, product_id)
);

-- Diaries table with BOOLEAN fields and correct spelling
CREATE TABLE IF NOT EXISTS Diaries (
    diary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date TIMESTAMP,
    product_id INTEGER,
    body_part TEXT,
    acne BOOLEAN,          
    adverse BOOLEAN,        
    diary_note TEXT,
    diary_photo TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Reviews table with BOOLEAN repurchase and timestamp
CREATE TABLE IF NOT EXISTS Reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    stars INTEGER CHECK(stars BETWEEN 1 AND 5),
    review_note TEXT,
    repurchase BOOLEAN,    
    review_photo TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    UNIQUE(user_id, product_id)
);

-- Reminders table 
CREATE TABLE IF NOT EXISTS Reminders (
    reminder_id INTEGER PRIMARY KEY AUTOINCREMENT,
    reminder_type TEXT,
    alarm_date DATETIME,
    recurrence FLOAT,  
    reminder_note TEXT,  
    user_id INTEGER NOT NULL,
    product_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Insert data into Users table
INSERT INTO Users (username, password, email, age, skintype, profile_pic) VALUES
('raisa', 'password123', 'raisa@gmail.com', 24, 'Oily', 'flower-corner.PNG'),
('admin', '123', 'admin@gmail.com', 23, 'Dry', 'default.png'),
('epicsaif', '123', 'epicsaif@gmail.com', 23, 'Dry', 'default.png');

INSERT INTO Users (username, password, email, age, skintype, profile_pic) VALUES
('skincareQueen', 'pass1234', 'queen@example.com', 25, 'oily', 'pic1.jpg'),
('glowGetter', 'glowUp2023', 'glow@example.com', 31, 'dry', 'pic2.jpg'),
('acneWarrior', 'securePass!', 'acne_w@example.com', 20, 'combination', 'pic3.jpg'),
('dewyDiva', 'dew2024', 'diva@example.com', 27, 'normal', 'pic4.jpg'),
('freshFace', 'fresh123', 'freshface@example.com', 22, 'sensitive', 'pic5.jpg');


-- Insert data into Products table 
INSERT INTO Products (product_name, type, amazon_link, directions, shelflife, ingredients) VALUES
('Vitamin A', 'Other', 'https://www.amazon.com/Nutricost-Vitamin-000-Softgel-Capsules/dp/B01HQLCYW2/ref=sr_1_1_sspa?crid=11WEYJTXW8MLY&dib=eyJ2IjoiMSJ9.W-F7hK13T9ZpDnUq6tBE68V1a7ogN3AqPHYRB37qeqtDZIhmVakpQLLTDiHs073L-GeoCJgQt1kMWJ9UmzkKp7MEW3k2JgOYLM77cUvt5G8Wh7SDTjjMRSyOYG-qqcJ3d7q20x3V1XB1m3p9WKVHiHOpAIE9y59BD4yb8UnQBI8EmZtOSMAMK8cH7hHhL0gN5GuX76y0BVRzSxwFlAzUs2agOxrRdrQuMdEFty8wl8b6YzjyONLCHC1Bd3TqgK3J7YEBt7kaXzhTd3xjQtcMJisg0KwvrwfirLv5ghTBxJw.HmpvQUDVR2BGZx8fcFNON_E9XQj-wWcr9SSJF4bqWMQ&dib_tag=se&keywords=vitamin+A&qid=1745139809&sprefix=vitamin+a%2Caps%2C109&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1', 'Apply at night daily', 12, 'Zutaten: Sâuerungsmittel Citronensâure, Sâureregulator Natriumhydrogencarbonat, SüBungsmittel Sorbit, Maisstârke, Aromen, L-Ascorbinsàure (Vitamin C), Rote-Bete-Pulver, SüBungsmittel Natriumcyclamat und Saccharin-Natrium, DL-a-Tocopherylacetat R Pyridoxinhydrochlorid (Vitamin B6), Farbstoff Riboflavin, Riboflavin (VitaminB2), Tt (Folsàure), D-Biotin, Cyanocobalamin Vitamin B12)'),
('Sunscreen', 'Sunscreen', 'https://www.amazon.com/s?k=sunscreen+amazon&adgrpid=1345802802776174&hvadid=84112915028627&hvbmt=be&hvdev=c&hvlocphy=101633&hvnetw=o&hvqmt=e&hvtargid=kwd-84113031986407%3Aloc-190&hydadcr=28883_14568460&mcid=5a69379b03833892aea5f65e7763e7a9&msclkid=e59f3df7e4d01c264cda55f35c9ec8c4&tag=mh0b-20&ref=pd_sl_9d5ftqweyr_e', 'N/A', 6, 'Aqua, C12-15 Alkyl Benzoate, Glycerin, Ethylhexyl Triazone, Octocrylene, Butyl Methoxydibenzoylmethane, Ethylhexyl Salicylate, 1,2-Hexanediol, Diethylhexyl Butamido Triazone, Bis-Ethylhexyloxyphenol Methoxyphenyl Triazine, Phenylbenzimidazole Sulfonic Acid, Microcrystalline Cellulose, Cellulose Gum, Cetyl Alcohol, Sodium Stearoyl Glutamate, Sodium Chloride, Glyceryl Stearate, Parfum, Xanthan Gum, Tocopheryl Acetate, Tocopherol, Helianthus Annuus Seed Oil, Ethylhexylglycerin, Caprylyl Glycol, Decylene Glycol, Piroctone Olamine, Tetrasodium Iminodisuccinate, Sodium Hydroxide'),
('Vitamin C', 'Other', 'https://www.amazon.com/dp/B074GCB1ND?maas=maas_adg_89B21E116B4948D94F601335586D730B_afap_abs&ref_=aa_maas&tag=maas&msclkid=fb0f0d233fc016176178652787d8ab67&th=1', 'Apply in the morning', 6, 'Zutaten: Sâuerungsmittel Citronensâure, Sâureregulator Natriumhydrogencarbonat, SüBungsmittel Sorbit, Maisstârke, Aromen, L-Ascorbinsàure (Vitamin C), Rote-Bete-Pulver, SüBungsmittel Natriumcyclamat und Saccharin-Natrium, DL-a-Tocopherylacetat R Pyridoxinhydrochlorid (Vitamin B6), Farbstoff Riboflavin, Riboflavin (VitaminB2), Tt (Folsàure), D-Biotin, Cyanocobalamin Vitamin B12)'),
( 'Nivea Creme', 'Other', '#', 'N/A', 6, 'Aqua, Paraffinum Liquidum, Cera Microcrystallina, Glycerin, Lanolin Alcohol, Paraffin, Panthenol, Decyl Oleate, Octyldodecanol, Alumnium Stearate, Citric Acid, Magnesium Sulfate, Magnesium Stearate, Parfum, Limonene, Geraniol, Hydroxycitronellol, Linalool, Citronellol, Benzyl Benzoate, Cinnamyl Alcohol.'),
( 'Aveeno cream', 'Unknown', '#', 'N/A', 6, 'N/A');

INSERT INTO Products (product_name, type, amazon_link, directions, shelflife, ingredients) VALUES
('CeraVe Cleanser', 'cleanser', 'https://amazon.com/cerave-cleanser', 'Use morning and night.', 12, 'ceramides, niacinamide'),
('Neutrogena Sunscreen', 'sunscreen', 'https://amazon.com/neutrogena-spf50', 'Apply 15 minutes before sun.', 18, 'avobenzone, octocrylene'),
('The Ordinary Niacinamide', 'serum', 'https://amazon.com/ordinary-niacinamide', 'Apply before moisturizer.', 12, 'niacinamide, zinc PCA'),
('La Roche-Posay Moisturizer', 'moisturizer', 'https://amazon.com/la-roche-moist', 'Apply after cleansing.', 24, 'shea butter, glycerin'),
('Paulas Choice BHA', 'exfoliant', 'https://amazon.com/paulas-choice-bha', 'Use every other night.', 24, 'salicylic acid, green tea');

INSERT INTO Products (product_name, type, amazon_link, directions, shelflife, ingredients) VALUES
('Cerave Moisturizing Cream','Moisturizer','https://www.amazon.com/CeraVe-Moisturizing-Moisturizer-Niacinamide-Comedogenic/dp/B0CTTDLQF3/ref=sr_1_10?...','Apply to face and body as needed.',18,'Water, Ceramides, Glycerin'),
('Cerave Facial Moisturizing Lotion SPF 30','Sunscreen','https://www.amazon.com/CeraVe-Moisturizing-Cream-Daily-Moisturizer/dp/B00TTD9BRC/ref=sr_1_5?...','Apply 15 minutes before sun exposure.',12,'Water, Zinc Oxide, Ceramides'),
('Niacinamide','Serum','https://www.amazon.com/dp/B079DFPZPJ','Apply morning and night',12,'Niacinamide, Zinc PCA, Water'),
('Salicylic Acid','Cleanser','https://www.amazon.com/dp/B00LW2GM84','Use in evening',9,'Salicylic Acid, Glycerin, Water');



-- Insert sample collections
INSERT INTO Collections (user_id, product_id, created_at) VALUES
(1, 1, '2024-11-01 10:00:00'),
(1, 2, '2024-11-02 10:05:00'),
(2, 3, '2025-01-05 11:00:00'),
(3, 2, '2025-02-12 08:15:00'),
(4, 5, '2025-03-22 13:25:00'),
(5, 4, '2025-04-02 09:35:00');

-- Insert sample diary entries
INSERT INTO Diaries (user_id, date, product_id, body_part, acne, adverse, diary_note, diary_photo) VALUES
(1, '2025-04-20 09:00:00', 1, 'face', 2, 0, 'Skin feels smooth after wash.', 'diary1.jpg'),
(2, '2025-04-19 08:30:00', 3, 'forehead', 1, 0, 'Noticed less redness today.', 'diary2.jpg'),
(3, '2025-04-18 21:00:00', 2, 'cheeks', 4, 1, 'Feels greasy, slight breakout.', 'diary3.jpg'),
(4, '2025-04-20 07:45:00', 5, 'chin', 3, 0, 'Tingling sensation but tolerable.', 'diary4.jpg'),
(5, '2025-04-19 22:00:00', 4, 'neck', 0, 0, 'Soothing, no irritation.', 'diary5.jpg');

-- Insert sample reviews
INSERT INTO Reviews (user_id, product_id, stars, review_note, repurchase, review_photo) VALUES
(1, 1, 5, 'Love how gentle it is.', 1, 'review1.jpg'),
(2, 3, 4, 'Nice serum but takes time.', 1, 'review2.jpg'),
(3, 2, 2, 'Made my skin worse.', 0, 'review3.jpg'),
(4, 5, 5, 'Game-changer for my skin!', 1, 'review4.jpg'),
(5, 4, 4, 'Moisturizing and non-greasy.', 1, 'review5.jpg');


-- Insert sample reminders
INSERT INTO Reminders (reminder_type, alarm_date, recurrence, user_id, product_id) VALUES
('Morning Routine', '2025-04-21 08:00:00', 1, 1, 1),
('Night Serum', '2025-04-21 21:00:00', 1, 2, 3),
('Sunscreen', '2025-04-21 13:00:00', 1, 3, 2),
('Exfoliation', '2025-04-22 20:00:00', 7, 4, 5),
('Moisturize Neck', '2025-04-21 09:00:00', 0.5, 5, 4);


-- Enable foreign key checks and commit the transaction
PRAGMA foreign_keys = ON;
