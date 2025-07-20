-- questions_data.sql

-- Insert topics
INSERT INTO topics (name) VALUES ('Software Engineering');
INSERT INTO topics (name) VALUES ('Healthcare');
INSERT INTO topics (name) VALUES ('Entrepreneurship Leadership');

-- Insert Healthcare questions (use topic_id = 2, assuming order above)
INSERT INTO questions (topic_id, question, option_a, option_b, option_c, option_d, correct_option) VALUES
(2, 'What is the largest organ in the human body?', 'Brain', 'Skin', 'Liver', 'Heart', 'B'),
(2, 'Which system is responsible for transporting blood in the body?', 'Respiratory', 'Digestive', 'Circulatory', 'Nervous', 'C'),
(2, 'What is the primary function of red blood cells?', 'Fight infection', 'Transport oxygen', 'Digest food', 'Store energy', 'B'),
(2, 'Which organ produces insulin?', 'Liver', 'Pancreas', 'Kidney', 'Stomach', 'B'),
(2, 'Which vitamin is essential for blood clotting?', 'A', 'D', 'K', 'C', 'C'),
(2, 'What is the term for the body’s ability to maintain internal stability?', 'Immunity', 'Regulation', 'Homeostasis', 'Metabolism', 'C'),
(2, 'Which of these professionals is NOT typically part of a hospital surgical team?', 'Surgeon', 'An anesthesiologist', 'Radiographer', 'Scrub nurse', 'C'),
(2, 'What is the function of white blood cells?', 'Oxygen transport', 'Fat storage', 'Fighting infections', 'Clotting', 'C'),
(2, 'What part of the brain controls balance and coordination?', 'Cerebrum', 'Medulla', 'Hypothalamus', 'Cerebellum', 'D'),
(2, 'Which field focuses on community health and preventing disease?', 'Surgery', 'Internal Medicine', 'Public Health', 'Psychiatry', 'C'),
(2, 'Which test is commonly used to diagnose malaria?', 'ECG', 'Blood smear', 'Urine test', 'MRI', 'B'),
(2, 'Which of the following is NOT a symptom of diabetes?', 'Excessive thirst', 'Frequent urination', 'Blurred vision', 'High calcium levels', 'D'),
(2, 'Which organ is primarily responsible for detoxifying harmful substances?', 'Kidney', 'Liver', 'Stomach', 'Intestine', 'B'),
(2, 'Which term describes an outbreak of disease across a large region or globally?', 'Endemic', 'Epidemic', 'Pandemic', 'Zoonotic', 'C'),
(2, 'Which of the following diseases is caused by a virus?', 'Tuberculosis', 'Malaria', 'HIV/AIDS', 'Typhoid', 'C'),
(2, 'Which device is used to measure blood pressure?', 'Thermometer', 'Sphygmomanometer', 'Stethoscope', 'Pulse oximeter', 'B'),
(2, 'Which health worker is trained to assist in childbirth?', 'Radiographer', 'Midwife', 'Dentist', 'Pathologist', 'B'),
(2, 'Which term refers to the basic health services provided to all individuals?', 'Advanced care', 'Emergency care', 'Primary healthcare', 'Specialist care', 'C'),
(2, 'What is antimicrobial resistance (AMR)?', 'Viruses that can''t be treated', 'Bacteria that resist antibiotics', 'Allergic reactions to vaccines', 'Cancer resistance', 'B'),
(2, 'Which global organization coordinates international public health efforts?', 'UNHCR', 'WHO', 'IMF', 'CDC', 'B');

-- [Add the rest of Healthcare questions here, topic_id=2]

-- Insert Software Engineering questions (topic_id = 1)
INSERT INTO questions (topic_id, question, option_a, option_b, option_c, option_d, correct_option) VALUES
(1, 'What does "HTML" stand for?', 'High Text Machine Language', 'HyperText Markup Language', 'Hyperlink and Text Markup Language', 'Home Tool Markup Language', 'B'),
(1, 'What is the primary purpose of an IDE in programming?', 'To design graphics', 'To compile code only', 'To manage databases', 'To write, compile, and debug code', 'D'),
(1, 'What is the main function of an operating system?', 'Manage social media', 'Translate programming languages', 'Manage hardware and software resources', 'Clean up your desktop', 'C'),
(1, 'Which language is commonly used for developing iOS apps?', 'Kotlin', 'Swift', 'Java', 'Ruby', 'B'),
(1, 'Which language is often used for data science and AI projects?', 'C++', 'Ruby', 'Python', 'PHP', 'C'),
(1, 'What does "Git" help developers do?', 'Manage internet browsers', 'Draw graphics', 'Track and manage code versions', 'Store files', 'C'),
(1, 'What is an API?', 'Application Programming Interface', 'Automated Performance Index', 'Advanced Programming Intelligence', 'Application Protocol Interface', 'A'),
(1, 'Which of the following is a markup language, not a programming language?', 'C++', 'Java', 'Python', 'HTML', 'D'),
(1, 'Which programming language is known for being used in front-end web development?', 'Java', 'JavaScript', 'Python', 'SQL', 'B'),
(1, 'What does CSS control on a webpage?', 'Database', 'Server performance', 'Style and layout', 'Backend logic', 'C'),
(1, 'What is meant by a "bug" in software?', 'A virus', 'An error in the program', 'A feature', 'A shortcut', 'B');

-- [Add the rest of Software Engineering questions here, topic_id=1]

-- Insert Entrepreneurship Leadership questions (topic_id = 3)
INSERT INTO questions (topic_id, question, option_a, option_b, option_c, option_d, correct_option) VALUES
(3, 'Which of the following best describes an entrepreneur?', 'A salaried employee', 'A business owner who takes risks to make profits', 'A manager in a large firm', 'A government worker', 'B'),
(3, 'Which is a key trait of successful entrepreneurs?', 'Avoiding risks', 'Preferring routine work', 'Willingness to innovate and adapt', 'Ignoring feedback', 'C'),
(3, 'Which of these is NOT a type of business ownership?', 'Sole proprietorship', 'Corporation', 'Monarchy', 'Partnership', 'C'),
(3, 'What is a business plan primarily used for?', 'Filing taxes', 'Seeking loans and investments', 'Hiring workers', 'Making company logos', 'B'),
(3, 'Which of these African tech entrepreneurs founded Flutterwave?', 'Strive Masiyiwa', 'Iyinoluwa Aboyeji', 'Aliko Dangote', 'Elon Musk', 'B');

-- [Add the rest of Entrepreneurship Leadership questions here, topic_id=3]
