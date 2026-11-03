-- Appropriate Index
CREATE INDEX idx_readings_machine_time
ON readings (machine_id, recorded_at DESC);

-- The order of columns is important because the database searches using the first column. Here, achine_id first and recorded_at second to make the query faster.

-- Explain  Analyze  executes the query , shows how much time it takes, whether an index is used and where the query is slow or fast.

-- Two disadvantages of unnecessary indexes. 
-- Indexes require extra storage space.
-- Indexes can slow other operations like INSERT, UPDATE and DELETE.