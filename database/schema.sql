-- MPLAD AI Monitoring System
-- Database Schema
-- PostgreSQL

CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    branch VARCHAR(100),
    college VARCHAR(200),
    target_role VARCHAR(100)
);

CREATE TABLE skills (
    skill_id SERIAL PRIMARY KEY,
    skill_name VARCHAR(100) NOT NULL,
    category VARCHAR(100),
    description TEXT
);

CREATE TABLE student_skills (
    student_skill_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    skill_id INT NOT NULL,
    skill_level VARCHAR(50),
    evidence TEXT,
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    project_name VARCHAR(200),
    project_description TEXT,
    technologies VARCHAR(500),
    project_url VARCHAR(500),
    FOREIGN KEY (student_id) REFERENCES student(student_id)
);

CREATE TABLE companies (
    company_id SERIAL PRIMARY KEY,
    company_name VARCHAR(200) NOT NULL,
    industry VARCHAR(100),
    location VARCHAR(200),
    website VARCHAR(500)
);

CREATE TABLE opportunities (
    opportunity_id SERIAL PRIMARY KEY,
    company_name VARCHAR(200),
    title VARCHAR(200),
    opportunity_type VARCHAR(100),
    description TEXT,
    required_skills TEXT,
    location VARCHAR(200),
    application_deadline DATE,
    company_id INT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE applications (
    application_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    opportunity_id INT NOT NULL,
    application_date DATE,
    status VARCHAR(50),
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (opportunity_id) REFERENCES opportunities(opportunity_id)
);

CREATE TABLE assessments (
    assessment_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    skill_id INT NOT NULL,
    score DECIMAL(5,2),
    assessment_date DATE,
    feedback TEXT,
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

CREATE TABLE skill_passport (
    passport_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    skill_id INT NOT NULL,
    proficiency_level VARCHAR(50),
    verification_status VARCHAR(50),
    evidence_source VARCHAR(200),
    last_updated DATE,
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

CREATE TABLE skill_gaps (
    gap_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    skill_id INT NOT NULL,
    required_level VARCHAR(50),
    current_level VARCHAR(50),
    gap_status VARCHAR(50),
    recommendation TEXT,
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

CREATE TABLE career_roles (
    role_id SERIAL PRIMARY KEY,
    role_name VARCHAR(150) NOT NULL,
    description TEXT
);

CREATE TABLE role_skills (
    role_skill_id SERIAL PRIMARY KEY,
    role_id INT NOT NULL,
    skill_id INT NOT NULL,
    required_level VARCHAR(50),
    FOREIGN KEY (role_id) REFERENCES career_roles(role_id),
    FOREIGN KEY (skill_id) REFERENCES skills(skill_id)
);

CREATE TABLE certifications (
    certification_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    certificate_name VARCHAR(200),
    issuing_organization VARCHAR(200),
    issue_date DATE,
    certificate_url VARCHAR(500),
    FOREIGN KEY (student_id) REFERENCES student(student_id)
);

CREATE TABLE internships (
    internship_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    company_id INT NOT NULL,
    title VARCHAR(200),
    start_date DATE,
    end_date DATE,
    status VARCHAR(50),
    certificate_url VARCHAR(500),
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);