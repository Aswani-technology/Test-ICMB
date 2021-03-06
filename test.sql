USE [Test]
GO
/****** Object:  StoredProcedure [dbo].[GETDATA]    Script Date: 6/11/2022 3:56:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[GETDATA]

AS
BEGIN
SELECT * FROM salesApp_salesteam

END
GO
/****** Object:  StoredProcedure [dbo].[INSERTDATA]    Script Date: 6/11/2022 3:56:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[INSERTDATA]

@firstname varchar(50),
@lastname varchar(50),
@email varchar(50),
@phone int,
@company varchar(50),
@hearabout varchar(50),
@comment varchar(50)

AS
BEGIN
INSERT INTO salesApp_salesteam(firstname,lastname,email,phone,company,hear_about_us,comment)
VALUES (@firstname,@lastname,@email,@phone,@company,@hearabout,@comment)
END

GO
/****** Object:  StoredProcedure [dbo].[SEARCH]    Script Date: 6/11/2022 3:56:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[SEARCH](@id AS INT)
AS
BEGIN
SELECT * FROM salesApp_salesteam
WHERE id=@id
END
GO
