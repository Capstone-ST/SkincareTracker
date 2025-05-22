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
    product_name TEXT NOT NULL,
    type TEXT,
    amazon_link TEXT,
    directions TEXT,
    shelflife INTEGER,
    ingredients TEXT,
    product_pic TEXT, 
    user_id INTEGER REFERENCES Users(user_id)
);

-- Collections table 
CREATE TABLE IF NOT EXISTS Collections (
    collection_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    created_at DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Diaries table  
CREATE TABLE IF NOT EXISTS Diaries (
    diary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date TIMESTAMP,
    product_id INTEGER,
    acne BOOLEAN,
    adverse BOOLEAN,
    diary_note TEXT,
    diary_photo TEXT,
    shared BOOLEAN,
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
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
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

-- Insert sample users
INSERT INTO Users (username, password, email, age, skintype, profile_pic) VALUES
('raisa', 'password123', 'raisa@gmail.com', 24, 'Oily', 'flower-corner.PNG'),
('admin', '123', 'admin@gmail.com', 23, 'Dry', 'default.png'),
('epicsaif', '123', 'epicsaif@gmail.com', 23, 'Dry', 'default.png'),
('skincareQueen', 'pass1234', 'queen@example.com', 25, 'oily', 'pic1.jpg'),
('glowGetter', 'glowUp2023', 'glow@example.com', 31, 'dry', 'pic2.jpg'),
('acneWarrior', 'securePass!', 'acne_w@example.com', 20, 'combination', 'pic3.jpg'),
('dewyDiva', 'dew2024', 'diva@example.com', 27, 'normal', 'pic4.jpg'),
('freshFace', 'fresh123', 'freshface@example.com', 22, 'sensitive', 'pic5.jpg');


-- Insert data into Products table 
INSERT INTO Products (product_id,product_name,type,amazon_link,directions,shelflife,ingredients,product_pic,user_id) VALUES 
 (1,'Cerave Hydrating Mineral Sunscreen','Sunscreen','https://www.amazon.com/Mineral-Sunscreen-Titanium-Dioxide-Sensitive/dp/B07KLY4RYG/ref=sr_1_1?dib=eyJ2IjoiMSJ9.__FlTOq33x1j00Vn5XDFUlZCFjx1LjAB0uziA3T3Zc1XLh9dN1aJp-2DsyHwF2EN-HLUfiYAVNxhhx2pxdDSVZm8UTRSntsFx1Qadjvihu6BJYRfvjgKUAj5tJelNDLRiABnwNtuGhn18MjZrCq_fvOVS8muTzQEJovli6HOYfkIWTCbrzzLZSzhDbPvDI_QQFlApg5emxYELBRmatgC_2sBOYWnT19Mqo29pzwOpSvWbsK4o9_jgVqsMkbotIGryIkY0d43WlqdcTVriroinPujbQOreRUOUfs6uB4xy6Q.F1-xBoKcPLbexPJGWKRvQClBn_Fm98mNmh4WmDoW_rk&dib_tag=se&hvadid=695557437755&hvdev=c&hvexpln=67&hvlocphy=9032538&hvnetw=g&hvocijid=6172648998554315581--&hvqmt=b&hvrand=6172648998554315581&hvtargid=kwd-2297494703977&hydadcr=28826_14753892&keywords=cerave+hydrating+mineral+spf+50&mcid=edc452f167533bbd8aca53b0ba1c3dbe&qid=1747863094&sr=8-1','N/A',12,'Active Ingredients: Titanium Dioxide (9%), Zinc Oxide (7%), Inactive Ingredients: Water, Glycerin, C12-15 Alkyl Benzoate, Dimethicone, Isododecane, Styrene/acrylates Copolymer, Glyceryl Stearate, Butyloctyl Salicylate, Dicaprylyl Carbonate, Propanediol, Stearic Acid, Aluminum Hydroxide, Peg-100 Stearate, Sorbitan Stearate, Niacinamide, Peg-8 Laurate, Ceramide NP, Ceramide AP, Ceramide EOP, Sorbitan Isostearate, Carbomer, Cetearyl Alcohol, Ceteareth-20, Triethoxycaprylylsilane, Dimethiconol, Sodium Citrate, Sodium Lauroyl Lactylate, Sodium Dodecylbenzenesulfonate, Myristic Acid, Sodium Hyaluronate, Cholesterol, Palmitic Acid, Phenoxyethanol, Chlorphenesin, Tocopherol, Hydroxyethyl Acrylate/sodium Acryloyldimethyl Taurate Copolymer, Caprylyl Glycol, Citric Acid, Panthenol, Xanthan Gum, Phytosphingosine, Polyhydroxystearic Acid, Polysorbate 60, Ethylhexylglycerin','cerave_mineral_spf.jpeg',NULL),
 (2,'Cerave Skin Renewing Vitamin C Serum','Other','https://www.amazon.com/CeraVe-Vitamin-Hyaluronic-Brightening-Fragrance/dp/B07PNCCLD2/ref=sr_1_7?crid=5SIYY69YKH9O&dib=eyJ2IjoiMSJ9.9K7RRY7JNclmtvNuoO1I_8DSzsgd4P47PTlHSsgJgCoO-41OJRk-yDJidKBUTCIH2AKF9sSaHLU0lBLZCfgu7FSIdkCytrRg5qF6ncWYD653H5AccP4kNBYSuiPDSFGxDMpABzvKlFgKedDn5f1RDLq3b1a3njsMhJkcmgN2TtDLDfhW_jvrlsWCRcRqz4twcrF8Iz8myXiY7OrYN9W4p4j2I05pkermPAY8p1aHrdzwL-wMYS-TvtXsh-gVp81QkjTx7bybeha3B4LHL9AmV8uWbWgKYM3SqHyAXGnTgec.YdGz69Q1IGqqOE-OsqpRRJ0nyo0HH03Zm1TmxRAoTJ0&dib_tag=se&keywords=vitamin+c+serum&qid=1747863196&s=hpc&sprefix=vitamin+c+serum%2Chpc%2C204&sr=1-7','Apply in the morning',6,'WATER, ASCORBIC ACID, GLYCERIN, DIMETHICONE, CETEARYL ETHYLHEXANOATE, ALCOHOL DENAT., SODIUM HYDROXIDE, AMMONIUM POLYACRYLOYLDIMETHYL TAURATE, PANTHENOL, CERAMIDE NP, CERAMIDE AP, CERAMIDE EOP, CARBOMER, CETEARYL ALCOHOL, BEHENTRIMONIUM METHOSULFATE, SODIUM HYALURONATE, SODIUM LAUROYL LACTYLATE, CHOLESTEROL, PHENOXYETHANOL, TOCOPHERYL ACETATE, DISODIUM EDTA, ISOPROPYL MYRISTATE, CAPRYLYL GLYCOL, XANTHAN GUM, PHYTOSPHINGOSINE, ETHYLHEXYLGLYCERIN','cerave_vitamin_c.webp',NULL),
 (3,'Nivea Creme','Moisturizer','https://www.amazon.com/NIVEA-Cr%C3%A8me-Unisex-Purpose-Moisturizing/dp/B00DEG8N9W/ref=sr_1_1?crid=HHRFKW4RRYB2&dib=eyJ2IjoiMSJ9.uO99nVhh3tVc8BXx_PfnQiutERGYOPZ5-dlk6lx0PqRp5-dvdWzzwZQ5uHIvkyomdW5mJGbMXuGnZDbWs5kmAaC14Nv2q0DrgJ3UlQGOTWRDnR7whTO1o5FIqIzPBgVT-de4uPsk2wr4hM7ND1HHO9-bnk08Bwbo67q0JWbZscjHEnKdWc3u2d0OxeMcbdtMHLb5qqZwDTMTm-8_IsrGq8ZxFXgiAABSa4Zb6lwX-4qS0a_BEzQb_eBeZPFRIaVBagJF59cj7vLqtMflctPu9e1IO7v_PV2CddV2tnzitoI.KzlkME-B0LuMyTVmcvT_NOP3vUUzG2f-jDAF7fpNHnQ&dib_tag=se&keywords=nivea+cream&qid=1747863905&sprefix=nivea%2Caps%2C164&sr=8-1','N/A',12,'Water, Mineral Oil, Petrolatum, Glycerin, Microcrystalline Wax, Lanolin Alcohol, Paraffin, Magnesium Sulfate, Decyl Oleate, Octyldodecanol, Aluminum Stearates, Fragrance, Panthenol, Citric Acid, Magnesium Stearate, Sodium Anisate','nivea_cream.jpeg',NULL),
 (4,'CeraVe Hydrating Foaming Oil Cleanser','cleanser','https://www.amazon.com/CeraVe-Hydrating-Moisturizing-Hyaluronic-Ceramides/dp/B0C7J55374/ref=sr_1_15?crid=EZP7NDAIVWVI&dib=eyJ2IjoiMSJ9.hmeMr7RGSvBYz94EX0rDPtOy3Ra1O1jR2PJH7erV2yC4KoJyCIc532EbvmRfZo_clmOhXNdOwaKbNZUX0EEQaRzK6ilppvlyscknEBEwhVNp5WREOezhVdEDHOeylfdhMJjxP_uKGHkzIcDCV9mW6Z3KVZzp4pxnteWTP6mZXsMOjvfIE6bm5pCPwTi-DZjM-uC0xzCux0BvcldDOPUX91gZg3oJXUAgbH_OQGsfA8p_MYycnW1LjUBs8oDEfAOpF8MOQGq3IGw_RkqNuTg-9RIVukWWMwOI2pPKR8TvMQY.b0IOKcZ88zhgwK5DA-0RTNR0wduFgI9G4ZUt4gFF2TY&dib_tag=se&keywords=cerave%2Bcleaner&qid=1747863817&sprefix=cerave%2Bcleaner%2Caps%2C198&sr=8-15&th=1','Use morning and night.',12,'AQUA/WATER, GLYCERIN, PEG-200 HYDROGENATED GLYCERYL PALMATE, COCO-BETAINE, DISODIUM COCOYL GLUTAMATE, PEG-120 METHYL GLUCOSE DIOLEATE, POLYSORBATE 20, PEG-7 GLYCERYL COCOATE, SQUALANE, CERAMIDE NP, CERAMIDE AP, CERAMIDE EOP, CARBOMER, TRIETHYL CITRATE, SODIUM CHLORIDE, SODIUM HYDROXIDE, SODIUM COCOYL GLUTAMATE, SODIUM BENZOATE, SODIUM LAUROYL LACTYLATE, SODIUM HYALURONATE, CHOLESTEROL, CITRIC ACID, CAPRYLOYL GLYCINE, HYDROXYACETOPHENONE, CAPRYLYL GLYCOL, CAPRYLIC/ CAPRIC TRIGLYCERIDE, TRISODIUM ETHYLENEDIAMINE DISUCCINATE, PHYTOSPHINGOSINE, XANTHAN GUM, BENZOIC ACID, PEG-150 PENTAERYTHRITYL TETRASTEARATE, PPG-5-CETETH-20, PEG-6 CAPRYLIC/CAPRIC GLYCERIDE','cerave_hydrating_cleanser.webp',NULL),
 (5,'Cerave Moisturizing Cream','Moisturizer','https://www.amazon.com/CeraVe-Moisturizing-Moisturizer-Niacinamide-Comedogenic/dp/B0CTTDLQF3/ref=sr_1_10?...','Apply to face and body as needed.',18,'AQUA / WATER / EAU, GLYCERIN, CETEARYL ALCOHOL, CAPRYLIC/CAPRIC TRIGLYCERIDE, CETYL ALCOHOL, CETEARETH-20, PETROLATUM, POTASSIUM PHOSPHATE, CERAMIDE NP, CERAMIDE AP, CERAMIDE EOP, CARBOMER, DIMETHICONE, BEHENTRIMONIUM METHOSULFATE, SODIUM LAUROYL LACTYLATE, SODIUM HYALURONATE, CHOLESTEROL, PHENOXYETHANOL, DISODIUM EDTA, DIPOTASSIUM PHOSPHATE, TOCOPHEROL, PHYTOSPHINGOSINE, XANTHAN GUM, ETHYLHEXYLGLYCERIN','cerave_moisturizing_cream.jpeg',NULL);
--  (6,'The Ordinary 10% Niacinamide + Zinc 1% Smoothing Serum','serum','https://www.amazon.com/Ordinary-Niacinamide-10-Zinc-30ml/dp/B01MDTVZTZ/ref=sr_1_1?crid=3DMUUGAY8FD9B&dib=eyJ2IjoiMSJ9.I4lyh0VPNo4VpF6XEbL_JwGxH64t5fU8AlFVB859EcdN3Ttgx3flKS_VkeNe9GjJdS6CksWb0DZIhWCnVQOwlZ-5SM8zcEWdv1a7K5U5J-Sv3rH065ZuZAvZeuJAPUkzRggtPCBKME9gcY0EawXqBDr7t1HgPc61ewMf-R0vj15WSLA0bMUQ03u3hQR0KGaE59q3SFnvJavgcGM6Xv47rPSPVDEprjSU0vo__GO_s8k8hF0DHOfRVtKe8hJc7D7uVsWxkhTCku031potu2ywZ35T097vxZJVr4-5iTfiGYY.Mo3M3r8iTgYTPFP7pyo9Rq5K9PoGhgvdy0p5d7j8F9E&dib_tag=se&keywords=the%2Bordinary%2Bniacinamide&qid=1747863702&sprefix=the%2Bordinary%2Caps%2C188&sr=8-1&th=1','Apply before moisturizer.',12,'niacinamide, zinc PCA','ordinary_niacinamide.webp',NULL),
--  (7,'La Roche-Posay Double Repair Face Moisturizer','moisturizer','https://www.amazon.com/Roche-Posay-Toleriane-Double-Repair-Moisturizer/dp/B01N9SPQHQ/ref=sr_1_5?crid=3LMD4V7N7MAGI&dib=eyJ2IjoiMSJ9.XVp9JLVKdRgJfGLiukEsCwo9zJOu2yNnIDtwSU6768xzYpWcRc6WzRPdfj4E2tNrMoGF3y1fs9j6--0poB-X6eGs3EFmPHQQIVjNvlDcwGSQ7fKpljlQpkk4GXUoXlTBUI3ZZuNRrFzwe7gUO17tcC4f2LLRUOSGAZEdPERk2eT6_BCOJsKPbjZHdCJ4a1ii4MdCMhPjVuMWuMvJ1PNCJrzYArW3tCaFVIgc3blsrKz1yFJe2sgdN6S_7p1tqxcSfqYvkFVR4qYtE9NuVC18HkLpWd9N1QMTBJ86Ml_l1_I.AscIMrkX1eP6PdH7ofoh_ZbxTbxhzv4ez9dc2JaanmI&dib_tag=se&keywords=la+roshe+posay+moisturizer&qid=1747863487&sprefix=la+ros%2Caps%2C168&sr=8-5','Apply after cleansing.',24,'shea butter, glycerin','lrp_double_repair_moisturizer.webp',NULL),
--  (8,'Paulas Choice BHA Facial Exfoliant','exfoliant','https://www.amazon.com/Paulas-Choice-SKIN-PERFECTING-Exfoliant-Facial-Blackheads/dp/B00949CTQQ/ref=sr_1_1?dib=eyJ2IjoiMSJ9.8Y3MmnA0KMJ1CuQfo7iq35svz-S_CZnT201v7SriBLzRbW75cbQWEoTk82KX1Shho35oPozLrC2zWyNSOs23edquul2DBo6CbFhubdnkFa5uK0LWudW-jLwLMnVfKAEk023LXtXJH0qM0kf-ynsezVC9xT5wLkVRNAWqzN7kBqEw83-TqXiIytdTy6jnUxRuAexMBTK7VxRPIF7R8PN13rDl3sc0--HIN9wZKwniErViZ_HCARhTmgO4yUNdj4vapf0eN_2F0YytfYmyWG6ctvnlMvZIBU8y36IuRkY0fEs.iN2LkZvM2baeJsBEqhBdc7Zk-WBEJHFoRPLtqYBjOTg&dib_tag=se&keywords=paulas%2Bchoice%2Bbh&qid=1747863449&sr=8-1&th=1','Use every other night.',24,'salicylic acid, green tea', 'paulas_choice.jpeg',NULL),
--  (9,'Neutrogena Ultra Sheer Face Serum Sunscreen','sunscreen','https://www.amazon.com/Neutrogena-Moisturizing-Protection-Fragrance-Free-Oxybenzone-Free/dp/B09MV3MHJD/ref=sr_1_2_sspa?crid=HT4S7NYA7JQL&dib=eyJ2IjoiMSJ9.78xNKGmWt0sfjQhTrH8oCglw9TPZwMwJGYqu6BxnyoFfDeTua0t8o4xBTa8nVPzjcrQX5C3e5vUacflX7EFa8WR_uRv1QXwrdIGfUWNZ65DKTshUt6Ishz-z1hHCmTk0-uhNYWIHgU92VsxvGMvGZrQpIm0eG3aofnLWhmMl0dRNF1nmgkdXwIIYXT5y-ildefav9izRAWQVv1GSipZf3c3_gkcpC8II9asTWhySqA20KetaoI26wiZ0uXOWNXYp8BA7838WlAtEffOJXCvgTr0KEHINV89Zo4u5bl1YPrs.QTdR_o0DqoWlU9ozqzROJkrH_teLDJsS-LSDeJd3Vkk&dib_tag=se&keywords=neutrogena+sunscreen&qid=1747863779&sprefix=neutro%2Caps%2C256&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1','Apply 15 minutes before sun.',18,'avobenzone, octocrylene','neutrogena_sheer_spf.jpeg',NULL);
--  (10,'Cerave Facial Moisturizing Lotion SPF 30','Sunscreen','https://www.amazon.com/CeraVe-Moisturizing-Cream-Daily-Moisturizer/dp/B00TTD9BRC/ref=sr_1_5?...','Apply 15 minutes before sun exposure.',12,'Water, Zinc Oxide, Ceramides','cerave_facial_moisturizin_lotion.jpeg',NULL);


-- Insert sample collections
INSERT INTO Collections (user_id, product_id, created_at) VALUES
(1, 1, '2024-11-01 10:00:00'),
(1, 2, '2024-11-02 10:05:00'),
(1, 3, '2025-01-05 11:00:00'),
(1, 2, '2025-02-12 08:15:00'),
(1, 5, '2025-03-22 13:25:00'),
(1, 4, '2025-04-02 09:35:00');

-- Insert sample diary entries
INSERT INTO Diaries (user_id, date, product_id, acne, adverse, diary_note, diary_photo, shared) VALUES
(1, '2025-04-20 09:00:00', 1, 1, 0, 'Skin feels smooth after wash.', 'diary1.jpg', 0),
(1, '2025-04-19 08:30:00', 3, 1, 0, 'Noticed less redness today.', 'diary2.jpg', 1),
(1, '2025-04-18 21:00:00', 2, 1, 1, 'Feels greasy, slight breakout.', 'diary3.jpg', 1),
(1, '2025-04-20 07:45:00', 5, 1, 0, 'Tingling sensation but tolerable.', 'diary4.jpg', 1),
(1, '2025-04-19 22:00:00', 4, 0, 0, 'Soothing, no irritation.', 'diary5.jpg', 0);

-- Insert sample reviews
INSERT INTO Reviews (user_id, product_id, stars, review_note, repurchase, review_photo) VALUES
(1, 1, 5, 'Love how gentle it is.', 1, 'review1.jpg'),
(2, 3, 4, 'Nice serum but takes time.', 1, 'review2.jpg'),
(3, 2, 2, 'Made my skin worse.', 0, 'review3.jpg'),
(4, 5, 5, 'Game-changer for my skin!', 1, 'review4.jpg'),
(5, 4, 4, 'Moisturizing and non-greasy.', 1, 'review5.jpg');


-- Insert sample reminders
INSERT INTO Reminders (reminder_type, alarm_date, recurrence, user_id, product_id) VALUES
('Morning Routine', '2025-05-28 08:00:00', 1, 1, 1),
('Night Serum', '2025-06-01 21:00:00', 1, 1, 3),
('Sunscreen', '2025-05-25 13:00:00', 1, 1, 2),
('Exfoliation', '2025-06-03 20:00:00', 7, 1, 5),
('Moisturize Neck', '2025-05-29 09:00:00', 0.5, 1, 4);


-- Enable foreign key checks and commit the transaction
PRAGMA foreign_keys = ON;
