-- Insert bear data into the bears table
INSERT INTO bears (name, age, sex, color, temperament, alive) VALUES
  ('Mr. Chocolate', 5, 'M', 'Brown', 'Friendly', 1),
  ('Rowdy', 3, 'M', 'Black', 'Aggressive', 1),
  ('Tabitha', 4, 'F', 'White', 'Playful', 1),
  ('Sergeant Brown', 6, 'M', 'Brown', 'Disciplined', 1),
  ('Melissa', 2, 'F', 'Red', 'Shy', 1),
  ('Grinch', 7, 'M', 'Green', 'Grumpy', 1),
  ('Wendy', 4, 'F', 'Pink', 'Gentle', 1);

-- Insert the unnamed bear separately
INSERT INTO bears (name, age, sex, color, temperament, alive) VALUES (NULL, NULL, NULL, NULL, NULL, 1);
