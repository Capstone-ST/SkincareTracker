-- Drop tables if they exist to avoid conflict
DROP TABLE IF EXISTS Reviews, Diaries, Reminders, Collections, Products, Users;

-- Create Users table
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    age INT,
    skintype VARCHAR(100),
    profile_pic VARCHAR(255)
);

INSERT INTO Users (username, password, email, age, skintype, profile_pic) VALUES
('raisa','password123','raisa@gmail.com',24,'Oily','flower-corner.PNG'), 
('admin','123','admin@gmail.com',23,'Dry','default.png'), 
('epicsaif','123','epicsaif@gmail.com',23,'Dry','default.png'), 
('skincareQueen','pass1234','queen@example.com',25,'oily','pic1.jpg'), 
('glowGetter','glowUp2023','glow@example.com',31,'dry','pic2.jpg'), 
('acneWarrior','securePass!','acne_w@example.com',20,'combination','pic3.jpg'), 
('dewyDiva','dew2024','diva@example.com',27,'normal','pic4.jpg'), 
('freshFace','fresh123','freshface@example.com',22,'sensitive','pic5.jpg'), 
('jane','test123','test@test.com',25,'combination',NULL);

-- Create Products table
CREATE TABLE IF NOT EXISTS Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    type VARCHAR(100),
    amazon_link TEXT,
    directions TEXT,
    shelflife INT,
    ingredients TEXT,
    product_pic VARCHAR(255),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);



INSERT INTO Products (product_id,product_name,type,amazon_link,directions,shelflife,ingredients,product_pic,user_id) VALUES
(1,'Cerave Hydrating Mineral Sunscreen','Sunscreen','https://www.amazon.com/Mineral-Sunscreen-Titanium-Dioxide-Sensitive/dp/B07KLY4RYG/ref=sr_1_1?dib=eyJ2IjoiMSJ9.__FlTOq33x1j00Vn5XDFUlZCFjx1LjAB0uziA3T3Zc1XLh9dN1aJp-2DsyHwF2EN-HLUfiYAVNxhhx2pxdDSVZm8UTRSntsFx1Qadjvihu6BJYRfvjgKUAj5tJelNDLRiABnwNtuGhn18MjZrCq_fvOVS8muTzQEJovli6HOYfkIWTCbrzzLZSzhDbPvDI_QQFlApg5emxYELBRmatgC_2sBOYWnT19Mqo29pzwOpSvWbsK4o9_jgVqsMkbotIGryIkY0d43WlqdcTVriroinPujbQOreRUOUfs6uB4xy6Q.F1-xBoKcPLbexPJGWKRvQClBn_Fm98mNmh4WmDoW_rk&dib_tag=se&hvadid=695557437755&hvdev=c&hvexpln=67&hvlocphy=9032538&hvnetw=g&hvocijid=6172648998554315581--&hvqmt=b&hvrand=6172648998554315581&hvtargid=kwd-2297494703977&hydadcr=28826_14753892&keywords=cerave+hydrating+mineral+spf+50&mcid=edc452f167533bbd8aca53b0ba1c3dbe&qid=1747863094&sr=8-1','N/A',12,'Active Ingredients: Titanium Dioxide (9%), Zinc Oxide (7%), Inactive Ingredients: Water, Glycerin, C12-15 Alkyl Benzoate, Dimethicone, Isododecane, Styrene/acrylates Copolymer, Glyceryl Stearate, Butyloctyl Salicylate, Dicaprylyl Carbonate, Propanediol, Stearic Acid, Aluminum Hydroxide, Peg-100 Stearate, Sorbitan Stearate, Niacinamide, Peg-8 Laurate, Ceramide NP, Ceramide AP, Ceramide EOP, Sorbitan Isostearate, Carbomer, Cetearyl Alcohol, Ceteareth-20, Triethoxycaprylylsilane, Dimethiconol, Sodium Citrate, Sodium Lauroyl Lactylate, Sodium Dodecylbenzenesulfonate, Myristic Acid, Sodium Hyaluronate, Cholesterol, Palmitic Acid, Phenoxyethanol, Chlorphenesin, Tocopherol, Hydroxyethyl Acrylate/sodium Acryloyldimethyl Taurate Copolymer, Caprylyl Glycol, Citric Acid, Panthenol, Xanthan Gum, Phytosphingosine, Polyhydroxystearic Acid, Polysorbate 60, Ethylhexylglycerin','cerave_mineral_spf.jpeg',NULL)
, (2,'Cerave Skin Renewing Vitamin C Serum','Other','https://www.amazon.com/CeraVe-Vitamin-Hyaluronic-Brightening-Fragrance/dp/B07PNCCLD2/ref=sr_1_7?crid=5SIYY69YKH9O&dib=eyJ2IjoiMSJ9.9K7RRY7JNclmtvNuoO1I_8DSzsgd4P47PTlHSsgJgCoO-41OJRk-yDJidKBUTCIH2AKF9sSaHLU0lBLZCfgu7FSIdkCytrRg5qF6ncWYD653H5AccP4kNBYSuiPDSFGxDMpABzvKlFgKedDn5f1RDLq3b1a3njsMhJkcmgN2TtDLDfhW_jvrlsWCRcRqz4twcrF8Iz8myXiY7OrYN9W4p4j2I05pkermPAY8p1aHrdzwL-wMYS-TvtXsh-gVp81QkjTx7bybeha3B4LHL9AmV8uWbWgKYM3SqHyAXGnTgec.YdGz69Q1IGqqOE-OsqpRRJ0nyo0HH03Zm1TmxRAoTJ0&dib_tag=se&keywords=vitamin+c+serum&qid=1747863196&s=hpc&sprefix=vitamin+c+serum%2Chpc%2C204&sr=1-7','Apply in the morning',6,'WATER, ASCORBIC ACID, GLYCERIN, DIMETHICONE, CETEARYL ETHYLHEXANOATE, ALCOHOL DENAT., SODIUM HYDROXIDE, AMMONIUM POLYACRYLOYLDIMETHYL TAURATE, PANTHENOL, CERAMIDE NP, CERAMIDE AP, CERAMIDE EOP, CARBOMER, CETEARYL ALCOHOL, BEHENTRIMONIUM METHOSULFATE, SODIUM HYALURONATE, SODIUM LAUROYL LACTYLATE, CHOLESTEROL, PHENOXYETHANOL, TOCOPHERYL ACETATE, DISODIUM EDTA, ISOPROPYL MYRISTATE, CAPRYLYL GLYCOL, XANTHAN GUM, PHYTOSPHINGOSINE, ETHYLHEXYLGLYCERIN','cerave_vitamin_c.webp',NULL)
, (3,'Nivea Creme','Moisturizer','https://www.amazon.com/NIVEA-Cr%C3%A8me-Unisex-Purpose-Moisturizing/dp/B00DEG8N9W/ref=sr_1_1?crid=HHRFKW4RRYB2&dib=eyJ2IjoiMSJ9.uO99nVhh3tVc8BXx_PfnQiutERGYOPZ5-dlk6lx0PqRp5-dvdWzzwZQ5uHIvkyomdW5mJGbMXuGnZDbWs5kmAaC14Nv2q0DrgJ3UlQGOTWRDnR7whTO1o5FIqIzPBgVT-de4uPsk2wr4hM7ND1HHO9-bnk08Bwbo67q0JWbZscjHEnKdWc3u2d0OxeMcbdtMHLb5qqZwDTMTm-8_IsrGq8ZxFXgiAABSa4Zb6lwX-4qS0a_BEzQb_eBeZPFRIaVBagJF59cj7vLqtMflctPu9e1IO7v_PV2CddV2tnzitoI.KzlkME-B0LuMyTVmcvT_NOP3vUUzG2f-jDAF7fpNHnQ&dib_tag=se&keywords=nivea+cream&qid=1747863905&sprefix=nivea%2Caps%2C164&sr=8-1','N/A',12,'Water, Mineral Oil, Petrolatum, Glycerin, Microcrystalline Wax, Lanolin Alcohol, Paraffin, Magnesium Sulfate, Decyl Oleate, Octyldodecanol, Aluminum Stearates, Fragrance, Panthenol, Citric Acid, Magnesium Stearate, Sodium Anisate','nivea_cream.jpeg',NULL)
, (4,'CeraVe Hydrating Foaming Oil Cleanser','cleanser','https://www.amazon.com/CeraVe-Hydrating-Moisturizing-Hyaluronic-Ceramides/dp/B0C7J55374/ref=sr_1_15?crid=EZP7NDAIVWVI&dib=eyJ2IjoiMSJ9.hmeMr7RGSvBYz94EX0rDPtOy3Ra1O1jR2PJH7erV2yC4KoJyCIc532EbvmRfZo_clmOhXNdOwaKbNZUX0EEQaRzK6ilppvlyscknEBEwhVNp5WREOezhVdEDHOeylfdhMJjxP_uKGHkzIcDCV9mW6Z3KVZzp4pxnteWTP6mZXsMOjvfIE6bm5pCPwTi-DZjM-uC0xzCux0BvcldDOPUX91gZg3oJXUAgbH_OQGsfA8p_MYycnW1LjUBs8oDEfAOpF8MOQGq3IGw_RkqNuTg-9RIVukWWMwOI2pPKR8TvMQY.b0IOKcZ88zhgwK5DA-0RTNR0wduFgI9G4ZUt4gFF2TY&dib_tag=se&keywords=cerave%2Bcleaner&qid=1747863817&sprefix=cerave%2Bcleaner%2Caps%2C198&sr=8-15&th=1','Use morning and night.',12,'AQUA/WATER, GLYCERIN, PEG-200 HYDROGENATED GLYCERYL PALMATE, COCO-BETAINE, DISODIUM COCOYL GLUTAMATE, PEG-120 METHYL GLUCOSE DIOLEATE, POLYSORBATE 20, PEG-7 GLYCERYL COCOATE, SQUALANE, CERAMIDE NP, CERAMIDE AP, CERAMIDE EOP, CARBOMER, TRIETHYL CITRATE, SODIUM CHLORIDE, SODIUM HYDROXIDE, SODIUM COCOYL GLUTAMATE, SODIUM BENZOATE, SODIUM LAUROYL LACTYLATE, SODIUM HYALURONATE, CHOLESTEROL, CITRIC ACID, CAPRYLOYL GLYCINE, HYDROXYACETOPHENONE, CAPRYLYL GLYCOL, CAPRYLIC/ CAPRIC TRIGLYCERIDE, TRISODIUM ETHYLENEDIAMINE DISUCCINATE, PHYTOSPHINGOSINE, XANTHAN GUM, BENZOIC ACID, PEG-150 PENTAERYTHRITYL TETRASTEARATE, PPG-5-CETETH-20, PEG-6 CAPRYLIC/CAPRIC GLYCERIDE','cerave_hydrating_cleanser.webp',NULL)
, (5,'Cerave Moisturizing Cream','Moisturizer','https://www.amazon.com/CeraVe-Moisturizing-Moisturizer-Niacinamide-Comedogenic/dp/B0CTTDLQF3/ref=sr_1_10?...','Apply to face and body as needed.',18,'AQUA / WATER / EAU, GLYCERIN, CETEARYL ALCOHOL, CAPRYLIC/CAPRIC TRIGLYCERIDE, CETYL ALCOHOL, CETEARETH-20, PETROLATUM, POTASSIUM PHOSPHATE, CERAMIDE NP, CERAMIDE AP, CERAMIDE EOP, CARBOMER, DIMETHICONE, BEHENTRIMONIUM METHOSULFATE, SODIUM LAUROYL LACTYLATE, SODIUM HYALURONATE, CHOLESTEROL, PHENOXYETHANOL, DISODIUM EDTA, DIPOTASSIUM PHOSPHATE, TOCOPHEROL, PHYTOSPHINGOSINE, XANTHAN GUM, ETHYLHEXYLGLYCERIN','cerave_moisturizing_cream.jpeg',NULL)
, (6,'Cetaphil Lotion ','Moisturizer','https://www.amazon.com/Intensive-Ceramides-Sensitive-Hydration-Dermatologist/dp/B07S7FRWKR?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&psc=1&smid=ATVPDKIKX0DER','N/A',6,'Aqua, glycerin, isopropyl palmitate, cetearyl alcohol, ceteareth-20, panthenol, niacinamide, tocopheryl acetate, dimethicone, persea gratissma (avocado) oil, helianthus annuus (sunflower) seed oil, glyceryl stearate, sodium benzoate, benzyl alcohol, citric acid, pantolactone fil 1745.','cetaphit_lotion_image.jpg',1);

-- Create Collections table
CREATE TABLE IF NOT EXISTS Collections (
    collection_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Collections (user_id, product_id, created_at) VALUES
(1, 1, '2024-11-01 10:00:00'),
(1, 1, '2024-11-02 10:05:00'),
(1, 1, '2025-01-05 11:00:00'),
(1, 1, '2025-02-12 08:15:00'),
(1, 1, '2025-03-22 13:25:00'),
(1, 1, '2025-04-02 09:35:00'),
(1, 1, '2025-05-30 23:05:55');

-- Create Diaries table
CREATE TABLE IF NOT EXISTS Diaries (
    diary_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    date TIMESTAMP,
    product_id INT,
    acne TINYINT(1),
    adverse TINYINT(1),
    diary_note TEXT,
    diary_photo VARCHAR(255),
    shared TINYINT(1),
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Diaries (user_id, date, product_id, acne, adverse, diary_note, diary_photo, shared) VALUES
(1, '2025-04-20 09:00:00', 1, 1, 0, 'Skin feels smooth after wash.', 'diary1.jpg', 0),
(1, '2025-04-19 08:30:00', 3, 1, 0, 'Noticed less redness today.', 'diary2.jpg', 1),
(1, '2025-04-18 21:00:00', 2, 1, 1, 'Feels greasy, slight breakout.', 'diary3.jpg', 1),
(1, '2025-04-20 07:45:00', 5, 1, 0, 'Tingling sensation but tolerable.', 'diary4.jpg', 1),
(1, '2025-04-19 22:00:00', 4, 0, 0, 'Soothing, no irritation.', 'diary5.jpg', 0);

-- Create Reviews table
CREATE TABLE IF NOT EXISTS Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    stars INT CHECK (stars BETWEEN 1 AND 5),
    review_note TEXT,
    repurchase TINYINT(1),
    review_photo VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Reviews (user_id, product_id, stars, review_note, repurchase, review_photo, created_at) VALUES
(1, 1, 5, 'Love how gentle it is.', 1, 'review1.jpg', '2025-05-22 21:24:22'),
(2, 2, 4, 'Nice serum but takes time.', 1, 'review2.jpg', '2025-05-22 21:24:22'),
(3, 3, 2, 'Made my skin worse.', 0, 'review3.jpg', '2025-05-22 21:24:22'),
(4, 4, 5, 'Game-changer for my skin!', 1, 'review4.jpg', '2025-05-22 21:24:22'),
(5, 5, 4, 'Moisturizing and non-greasy.', 1, 'review5.jpg', '2025-05-22 21:24:22'),
(6, 1, 5, 'A tiny bit greasy but overall very nourishing.', 1, NULL, '2025-05-30 23:53:31'),
(7, 1, 4, 'This is very good!', 1, NULL, '2025-05-30 23:55:59');

-- Create Reminders table
CREATE TABLE IF NOT EXISTS Reminders (
    reminder_id INT AUTO_INCREMENT PRIMARY KEY,
    reminder_type VARCHAR(255),
    alarm_date DATETIME,
    recurrence FLOAT,
    reminder_note TEXT,
    user_id INT NOT NULL,
    product_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Reminders (reminder_type, alarm_date, recurrence, reminder_note, user_id, product_id) VALUES
('Morning Routine', '2025-05-28 08:00:00', 1.0, NULL, 1, 1),
('Night Serum', '2025-06-01 21:00:00', 1.0, NULL, 1, 3),
('Sunscreen', '2025-05-25 13:00:00', 1.0, NULL, 1, 2),
('Exfoliation', '2025-06-03 20:00:00', 7.0, NULL, 1, 5),
('Moisturize Neck', '2025-05-29 09:00:00', 0.5, NULL, 1, 4),
('product shelf life / expiration', '2025-06-05 16:05:55', 6.0, NULL, 1, NULL);

