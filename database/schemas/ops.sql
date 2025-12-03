/*
  EARLY SCHEMA EXAMPLE for ops - OPS SCHEMA NOW MANAGED IN editorial dashboard (reporting pipeline repo)
*/


-- State + checkpoints live under ops.*
create schema if not exists ops;

-- one row per named component (e.g., 'schedule_a', 'schedule_b', 'candidates')
create table if not exists ops.ingest_state (
  name text,
  target varchar(50) default 'all',
  last_run timestamptz,
  updated_at timestamptz default now()
);

ALTER TABLE ops.ingest_state ADD PRIMARY KEY (name, target);
CREATE INDEX IF NOT EXISTS idx_ingest_state_name_target ON ops.ingest_state(name, target);

-- arbitrary JSON checkpoint per name (e.g., pagination cursor, last_index, etc.)
create table if not exists ops.ingest_checkpoints (
  name text,
  target varchar(50) default 'all',
  data jsonb not null default '{}',
  updated_at timestamptz default now()
);

ALTER TABLE ops.ingest_checkpoints ADD PRIMARY KEY (name, target);
CREATE INDEX IF NOT EXISTS idx_ingest_checkpoints_name_target ON ops.ingest_checkpoints(name, target);

-- per-committee last_run for schedules (e.g., 'schedule_a' + 'C00612345')
create table if not exists ops.committee_run_state (
  schedule_name text not null,
  committee_id  text not null,
  last_run timestamptz,
  updated_at timestamptz default now(),
  primary key (schedule_name, committee_id)
);

CREATE TABLE IF NOT EXISTS ops.committee_targets (
    id SERIAL PRIMARY KEY,
    committee_id VARCHAR(10) NOT NULL,
    committee_name VARCHAR(255),
    description TEXT,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Add some indexes
CREATE UNIQUE INDEX IF NOT EXISTS idx_committee_targets_committee_id ON ops.committee_targets(committee_id);
CREATE INDEX IF NOT EXISTS idx_committee_targets_active ON ops.committee_targets(active);
