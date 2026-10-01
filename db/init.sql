CREATE TABLE IF NOT EXISTS learning_topics (
    id SERIAL PRIMARY KEY,
    topic VARCHAR(100) NOT NULL,
    status VARCHAR(50) NOT NULL
);

INSERT INTO learning_topics (topic, status)
VALUES
    ('Linux', 'Completed'),
    ('Git', 'Completed'),
    ('Docker', 'Completed'),
    ('Docker Compose', 'Learning'),
    ('Kubernetes', 'Upcoming');
