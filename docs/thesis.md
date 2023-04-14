Perfect Parking

An AI Application to Assist Drivers Finding Parking in Busy Cities

Rhys Quilter

K00241356

A Final Year Project submitted as a requirement of the Technological
University of Shannon for the degree of Bachelor of Science (Honors) in
Software Development.

Supervised by:

John Jennings

# Acknowledgments

I would like to thank my supervisor Henry McCoy for helping me to
complete my research. In addition, I would like to thank my parents
Christopher and Katherine, and my friends Jean, Logan, and Warren for
all their support during my time at TUS.

# Abstract

This is a sample thesis layout with AI and Software development headings
to guide you in developing your thesis. It contains styles, formatting,
and a suggested structure with features like headers, footers,
page-numbers, Table of contents, Table of figures and managed
references.

It is a useful and common practice to put the abstract in Times New
Roman 12-point italics. Throughout this document the styles used reflect
the styles we suggest you use in your scientific report.

# Table of Contents

[Acknowledgments [ii](#acknowledgments)](#acknowledgments)

[Abstract [iii](#abstract)](#abstract)

[Table of Contents [iv](#table-of-contents)](#table-of-contents)

[Table of Figure [viii](#table-of-figure)](#table-of-figure)

[Chapter 1 Introduction [9](#introduction)](#introduction)

[1.1 The academic objectives
[9](#the-academic-objectives)](#the-academic-objectives)

[1.2 Problem Domain? [9](#problem-domain)](#problem-domain)

[1.3 Product title: a solution
[9](#product-title-a-solution)](#product-title-a-solution)

[1.4 Objectives [9](#objectives)](#objectives)

[1.5 The Scope of the solution
[9](#the-scope-of-the-solution)](#the-scope-of-the-solution)

[1.6 Report Structure [9](#report-structure)](#report-structure)

[Chapter 2 Materials [11](#materials)](#materials)

[2.1 Existing Data [11](#existing-data)](#existing-data)

[2.1.0 Others [11](#others)](#others)

[2.2 How we can choose [11](#how-we-can-choose)](#how-we-can-choose)

[2.2.1 Machine Learning [11](#machine-learning)](#machine-learning)

[2.3 Conclusion: The Need for a Software Solution
[11](#conclusion-the-need-for-a-software-solution)](#conclusion-the-need-for-a-software-solution)

[Chapter 3 Project Management
[12](#project-management)](#project-management)

[3.1 Weekly Meetings [12](#weekly-meetings)](#weekly-meetings)

[3.2 Source code management (SCM)
[12](#source-code-management-scm)](#source-code-management-scm)

[3.3 Code Style Guide [12](#code-style-guide)](#code-style-guide)

[3.4 Collaboration Tools
[12](#collaboration-tools)](#collaboration-tools)

[3.4.1 GitHub [12](#github)](#github)

[3.4.2 Microsoft Office Online
[12](#microsoft-office-online)](#microsoft-office-online)

[Chapter 4 Data Analytic Methods
[13](#data-analytic-methods)](#data-analytic-methods)

[4.1 Artificial Intelligence
[13](#artificial-intelligence)](#artificial-intelligence)

[4.2 Categorization [13](#categorization)](#categorization)

[4.3 Estimation [13](#estimation)](#estimation)

[4.4 Machine Learning [13](#machine-learning-1)](#machine-learning-1)

[4.4.1 Garbage in, likely garbage out
[13](#garbage-in-likely-garbage-out)](#garbage-in-likely-garbage-out)

[4.5 Working with Data Structures Object Orientated Programming
[13](#working-with-data-structures-object-orientated-programming)](#working-with-data-structures-object-orientated-programming)

[4.6 Examples [13](#examples)](#examples)

[4.7 Conclusion [13](#conclusion)](#conclusion)

[Chapter 5 Data Analysis [15](#data-analysis)](#data-analysis)

[5.1 Introduction and focus
[15](#introduction-and-focus)](#introduction-and-focus)

[5.2 Academic Aims [15](#academic-aims)](#academic-aims)

[5.2.1 Academic Requirements
[15](#academic-requirements)](#academic-requirements)

[5.3 Functional Requirements
[15](#functional-requirements)](#functional-requirements)

[5.4 Non-Functional Requirements
[15](#non-functional-requirements)](#non-functional-requirements)

[5.5 Statistics [15](#statistics)](#statistics)

[Chapter 6 Results [16](#results)](#results)

[6.1 Project Plan: Priorities and Milestones
[16](#project-plan-priorities-and-milestones)](#project-plan-priorities-and-milestones)

[6.1.0 The Data Structure
[16](#the-data-structure)](#the-data-structure)

[6.1.1 Populating the System with Data
[16](#populating-the-system-with-data)](#populating-the-system-with-data)

[6.1.2 Machine Learning [16](#machine-learning-2)](#machine-learning-2)

[6.1.3 Testing [16](#testing)](#testing)

[6.1.4 Paths to completion
[16](#paths-to-completion)](#paths-to-completion)

[6.2 Data Structures [16](#data-structures)](#data-structures)

[6.3 System Architecture
[16](#system-architecture)](#system-architecture)

[6.3.1 Object Identification
[16](#object-identification)](#object-identification)

[6.4 Machine Learning [16](#machine-learning-3)](#machine-learning-3)

[6.5 Conclusion [16](#conclusion-1)](#conclusion-1)

[Chapter 7 Implementation [17](#implementation)](#implementation)

[7.1 Standards and Best Practice
[17](#standards-and-best-practice)](#standards-and-best-practice)

[7.1.1 Object Orientated Programming
[17](#object-orientated-programming)](#object-orientated-programming)

[7.1.2 Source Control and versioning
[17](#source-control-and-versioning)](#source-control-and-versioning)

[7.2 Development Environment
[17](#development-environment)](#development-environment)

[7.3 Tools Used [17](#tools-used)](#tools-used)

[Chapter 8 Conclusion and Recommendations
[18](#conclusion-and-recommendations)](#conclusion-and-recommendations)

[8.1 Conclusion [18](#conclusion-2)](#conclusion-2)

[8.2 Recommendations [18](#recommendations)](#recommendations)

[References [19](#_Toc132388068)](#_Toc132388068)

[Glossary [20](#glossary)](#glossary)

[Appendix A Reflections [21](#reflections)](#reflections)

[A.1 Report Structure [21](#report-structure-1)](#report-structure-1)

[Appendix B Project Management
[22](#project-management-1)](#project-management-1)

[B.1 Report Structure [22](#report-structure-2)](#report-structure-2)

[B.2 Code Style Guide [22](#code-style-guide-1)](#code-style-guide-1)

[B.2.1 Naming conventions
[22](#naming-conventions)](#naming-conventions)

[B.2.2 Avoid magic constant numbers.
[22](#avoid-magic-constant-numbers.)](#avoid-magic-constant-numbers.)

[B.2.3 Variable naming [22](#variable-naming)](#variable-naming)

[B.2.4 Methods [22](#methods)](#methods)

[B.2.5 Imports [22](#imports)](#imports)

[B.2.6 Comments [22](#comments)](#comments)

[B.2.7 Documentation [22](#documentation)](#documentation)

[B.2.8 Classes [22](#classes)](#classes)

[B.2.9 Spacing, Indentation
[22](#spacing-indentation)](#spacing-indentation)

[B.2.10 Literals [22](#literals)](#literals)

[Appendix C Development Environment
[23](#development-environment-1)](#development-environment-1)

# Table of Figure

[Figure 1: School Logo [14](#_Toc132284083)](#_Toc132284083)

# Introduction

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs

## The academic objectives

"I designed the Exocomps to be problem solvers" ... "So, in a sense,
they are learning."\
-- Doctor Farallon and Commander Data, 2369

The academic objectives of this project are to study and gain experience
working with blah.

The chosen problem used for this study is blah. The proposed blah.

## Problem Domain?

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs

1.  Numbered Bullet list.

2.  Numbered Bullet list

3.  Numbered Bullet item.

    a.  Numbered Bullet item.

    b.  Numbered Bullet item.

4.  Numbered Bullet list

## Product title: a solution

## Objectives

## The Scope of the solution

## Report Structure

This document has cover pages ...

An Abstract

TOC and TOF are generated automatically.

The Chapters the following styles

Paragraphs are 12pt Aril Justified with 1.5-line spaces and 6pt before
with 3 pt after.

# Materials

## Existing Data

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

### Others

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## How we can choose

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

### Machine Learning

## Conclusion: The Need for a Software Solution 

# Project Management

under the headings of (i) sub-topic 1 (cf. 1.1.0), and (ii) sub-topic 2
(cf. 1.1.1)

## Weekly Meetings

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Source code management (SCM)

## Code Style Guide

## Collaboration Tools

### GitHub

### Microsoft Office Online

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

# Data Analytic Methods

under the headings of (i) sub-topic 1 (cf. 1.1.0), and (ii) sub-topic 2
(cf. 1.1.1)

## Artificial Intelligence

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Categorization

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Estimation

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Machine Learning

### Garbage in, likely garbage out

## Working with Data Structures Object Orientated Programming

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Examples

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Conclusion

This chapter has outlined the ...

![A picture containing shape Description automatically
generated](./images/thesis/media/image3.png){width="2.6041666666666665in"
height="2.6041666666666665in"}

Figure TUS Logo

[]{#_Toc132284083 .anchor}Figure : School Logo

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

# Data Analysis

## Introduction and focus 

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Academic Aims

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

-   Bullets

-   Bullets

### Academic Requirements

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Functional Requirements

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Non-Functional Requirements

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Statistics

# Results

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Project Plan: Priorities and Milestones

### The Data Structure

### Populating the System with Data

### Machine Learning

### Testing

### Paths to completion

## Data Structures

## System Architecture

### Object Identification

## Machine Learning

## Conclusion

This chapter has outlined the ...

# Implementation

## Standards and Best Practice

### Object Orientated Programming

### Source Control and versioning

The solutions presented in this chapter are the best practices and
patterns of all those tried in various versions throughout the
lifecycles of the systems defines in section 1.2.

## Development Environment

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Tools Used

This chapter has outlined the ...

# Conclusion and Recommendations

## Conclusion

This chapter will begin by outlining the (cf. 1.1) for the purpose of
writing a Report for a Project and outlining paragraphs.

## Recommendations

-   This chapter will begin by outlining the (cf. 1.1) for the purpose
    of writing a Report for a Project and outlining paragraphs.

```{=html}
<!-- -->
```
-   This chapter will begin by outlining the (cf. 1.1) for the purpose
    of writing a Report for a Project and outlining paragraphs.

-   This chapter will begin by outlining the (cf. 1.1) for the purpose
    of writing a Report for a Project and outlining paragraphs.

-   This chapter will begin by outlining the (cf. 1.1) for the purpose
    of writing a Report for a Project and outlining paragraphs.

-   This chapter will begin by outlining the (cf. 1.1) for the purpose
    of writing a Report for a Project and outlining paragraphs.

```{=html}
<!-- -->
```
-   This chapter will begin by outlining the (cf. 1.1) for the purpose
    of writing a Report for a Project and outlining paragraphs.

-   This chapter will begin by outlining the (cf. 1.1) for the purpose
    of writing a Report for a Project and outlining paragraphs.

-   This chapter will begin by outlining the (cf. 1.1) for the purpose
    of writing a Report for a Project and outlining paragraphs.

# References

**There are no sources in the current document.**

# Glossary

  ------------------ ----------------------------------------------------
  Term 1             This chapter will begin by outlining the (cf. 1.1)
                     for the purpose of writing a Report for a Project
                     and outlining paragraphs

  Term 1             This chapter will begin by outlining the (cf. 1.1)
                     for the purpose of writing a Report for a Project
                     and outlining paragraphs

  Term 1             This chapter will begin by outlining the (cf. 1.1)
                     for the purpose of writing a Report for a Project
                     and outlining paragraphs
  ------------------ ----------------------------------------------------

# Reflections {#reflections .Appendix:-H1}

## Report Structure {#report-structure-1 .Appendix:-H2}

# Project Management {#project-management-1 .Appendix:-H1}

\"I bring order to chaos\" - The Borg Queen, 2373

A few sentences about how the project was managed. A bit about the code,
the document, the research, budget and timing, management frameworks and
so on.

## Report Structure {#report-structure-2 .Appendix:-H2}

## Code Style Guide {#code-style-guide-1 .Appendix:-H2}

\"This appears to be a region of space that doesn\'t have many rules.
But I believe we can learn something from the events that have unfolded.
In a part of space where there are few rules, it\'s more important than
ever that we hold fast to our own.\" -- Captain Janeway, 2372

### Naming conventions {#naming-conventions .Appendix:-H3}

### Avoid magic constant numbers. {#avoid-magic-constant-numbers. .Appendix:-H3}

### Variable naming {#variable-naming .Appendix:-H3}

### Methods {#methods .Appendix:-H3}

### Imports {#imports .Appendix:-H3}

### Comments {#comments .Appendix:-H3}

### Documentation {#documentation .Appendix:-H3}

### Classes {#classes .Appendix:-H3}

### Spacing, Indentation {#spacing-indentation .Appendix:-H3}

### Literals {#literals .Appendix:-H3}

# Development Environment {#development-environment-1 .Appendix:-H1}
