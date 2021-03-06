#
# $FreeBSD$
# $Id$
#

PORTNAME=       freenas-ui
PORTVERSION=    ${PRODUCT_VERSION:C/\-.*//:C/\_.*//}
PORTREVISION=	${REVISION}

CATEGORIES=     freenas
VALID_CATEGORIES+=	freenas

MAINTAINER=     dev@ixsystems.com
COMMENT=        FreeNAS UI

USE_XZ=		yes

USE_PYTHON=	yes

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}django:${PORTSDIR}/www/py-django \
	${PYTHON_PKGNAMEPREFIX}lxml:${PORTSDIR}/devel/py-lxml \
	${PYTHON_PKGNAMEPREFIX}xml:${PORTSDIR}/textproc/py-xml \
	${PYTHON_PKGNAMEPREFIX}bonjour:${PORTSDIR}/dns/py-bonjour \
	${PYTHON_PKGNAMEPREFIX}dnspython:${PORTSDIR}/dns/py-dnspython \
	${PYTHON_PKGNAMEPREFIX}requests:${PORTSDIR}/www/py-requests

EXTRACT_ONLY=
WRKSRC=/usr/freenasUI

NO_BUILD = yes

PLIST=		${WRKDIR}/plist

MAKE_JOBS_UNSAFE=yes

ALL_TARGET=obj all

checksum fetch:
	echo ${.TARGET} not needed because building direct

pre-install:
	${RM} -f ${PLIST}
	${ECHO_CMD} "@owner www"  >> ${PLIST}
	${ECHO_CMD} "@group www"  >> ${PLIST}
	${ECHO_CMD} "@comment files" >> ${PLIST}
	${FIND} ${WRKSRC} -type f | \
		${SED} -e 's|^/usr/|/www/|' -e 's|^/||' \
		| ${SORT} >> ${PLIST}
	${ECHO_CMD} www/freenasUI/local_settings.py >> ${PLIST}
	${ECHO_CMD} "@comment directories" >> ${PLIST}
	${FIND} ${WRKSRC} -type d \
		| ${SED} -e 's|^/usr/|/www/|' -e 's|^/||' -e 's|^|@dirrm |' \
		| ${SORT} -r >> ${PLIST}

do-install:
	${RM} -fr ${STAGEDIR}${PREFIX}/www/freenasUI
	${MKDIR} ${STAGEDIR}${PREFIX}/www/freenasUI
	${CP} -a ${WRKSRC}/ ${STAGEDIR}${PREFIX}/www/freenasUI
	${LN} -s -f /etc/local_settings.py ${STAGEDIR}${PREFIX}/www/freenasUI/local_settings.py

.include <bsd.port.mk>
