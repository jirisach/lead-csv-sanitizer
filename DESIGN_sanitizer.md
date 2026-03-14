# Design Decisions --- Lead CSV Sanitizer

Copyright 2026 Jiří Šach

This document explains the reasoning behind the architecture of **Lead
CSV Sanitizer**. The tool exists for one simple reason: prevent messy
lead data from entering CRM systems.

------------------------------------------------------------------------

## 1. Why a local CLI tool instead of a web application?

**Decision:** I designed the tool to run locally as a CLI utility.

**Reasoning:**

Lead datasets frequently contain sensitive customer information.

Uploading those datasets to a web service introduces unnecessary privacy
and compliance risk. Processing the data locally ensures that the
dataset never leaves the user's machine.

A CLI tool also has practical advantages:

-   zero infrastructure required
-   no internet dependency
-   instant usability for RevOps teams

Sometimes the most robust architecture is the one that avoids
infrastructure entirely.

------------------------------------------------------------------------

## 2. Why a deterministic processing pipeline?

**Decision:** I implemented a fixed processing order:

    normalize → validate → deduplicate → score → export

**Reasoning:**

Deterministic pipelines produce consistent results. The same dataset
should always produce the same output.

This improves:

-   debugging
-   testing
-   trust in the results

Non‑deterministic pipelines can behave unpredictably depending on
execution order. Predictability is a major advantage when dealing with
messy real‑world data.

------------------------------------------------------------------------

## 3. Why a Data Health Score as the primary metric?

**Decision:** I summarize dataset quality as a percentage score.

**Reasoning:**

RevOps professionals rarely want to read a long technical report before
importing leads.

A single score provides a fast signal about dataset quality:

-   high score → dataset likely safe to import
-   medium score → cleanup recommended
-   low score → dataset likely problematic

The score acts as an early warning system before bad data reaches the
CRM.

------------------------------------------------------------------------

## 4. Why normalize phone numbers to E.164?

**Decision:** I normalize phone numbers to the E.164 international
format.

**Reasoning:**

Phone numbers appear in countless formats depending on region and user
input:

    +420 777 123 456
    00420 777 123 456
    777123456

E.164 provides a single consistent representation. This improves:

-   duplicate detection
-   interoperability with CRM systems
-   compatibility with telephony services

Standardization removes ambiguity.

------------------------------------------------------------------------

## 5. Why detect duplicates using email and phone?

**Decision:** I use email and phone number as identity signals for
duplicate detection.

**Reasoning:**

Email addresses typically act as the primary identifier in CRM systems.
Phone numbers provide a secondary identity signal.

Using both signals increases detection accuracy and reduces the risk of
importing duplicate contacts into the CRM.

------------------------------------------------------------------------

## 6. Why minimize external dependencies?

**Decision:** I implemented core logic primarily using standard Python
libraries.

**Reasoning:**

Reducing dependencies simplifies:

-   installation
-   long‑term maintenance
-   security management

It also allows the tool to run reliably in restricted environments.

------------------------------------------------------------------------

## 7. Additional design decision

**Decision:** I generate a structured report alongside the cleaned
dataset.

**Reasoning:**

Cleaning data is only half the job. Understanding what went wrong with
the dataset is equally important.

Reports highlight:

-   duplicates
-   invalid fields
-   missing values

This gives teams visibility into data quality issues and helps improve
upstream data collection.

------------------------------------------------------------------------

*Maintained and updated by the author whenever the sanitizer evolves.*
