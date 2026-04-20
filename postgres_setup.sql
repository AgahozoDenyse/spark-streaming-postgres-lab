-- ============================================
-- PostgreSQL Setup for Real-Time Streaming Lab
-- ============================================

-- 1. Create Database
CREATE DATABASE events_db;

-- Connect to the database
\c events_db;

-- ============================================
-- 2. Create Table
-- ============================================

CREATE TABLE IF NOT EXISTS user_events (
    event_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    event_type VARCHAR(20) NOT NULL,
    product_id INT NOT NULL,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    event_time TIMESTAMP NOT NULL,
    event_hour INT
);

-- ============================================
-- 3. Indexes for Performance
-- ============================================

-- Index on timestamp (for time-based queries)
CREATE INDEX idx_event_time ON user_events(event_time);

-- Index on user_id (for user analytics)
CREATE INDEX idx_user_id ON user_events(user_id);

-- Index on event_type (for filtering)
CREATE INDEX idx_event_type ON user_events(event_type);

-- ============================================
-- 4. Optional: Sample Query for Testing
-- ============================================

-- SELECT * FROM user_events LIMIT 10;