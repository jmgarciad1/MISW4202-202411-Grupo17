def create_access_token(
    identity: Any,
    fresh: Fresh = False,
    expires_delta: Optional[ExpiresDelta] = None,
    additional_claims=None,
    additional_headers=None,
):
    """
    Create a new access token.

    :param identity:
        The identity of this token. It can be any data that is json serializable.
        You can use :meth:`~flask_jwt_extended.JWTManager.user_identity_loader`
        to define a callback function to convert any object passed in into a json
        serializable format.

    :param fresh:
        If this token should be marked as fresh, and can thus access endpoints
        protected with ``@jwt_required(fresh=True)``. Defaults to ``False``.

        This value can also be a ``datetime.timedelta``, which indicate
        how long this token will be considered fresh.

    :param expires_delta:
        A ``datetime.timedelta`` for how long this token should last before it
        expires. Set to False to disable expiration. If this is None, it will use
        the ``JWT_ACCESS_TOKEN_EXPIRES`` config value (see :ref:`Configuration Options`)

    :param additional_claims:
        Optional. A hash of claims to include in the access token.  These claims are
        merged into the default claims (exp, iat, etc) and claims returned from the
        :meth:`~flask_jwt_extended.JWTManager.additional_claims_loader` callback.
        On conflict, these claims take precedence.

    :param headers:
        Optional. A hash of headers to include in the access token. These headers
        are merged into the default headers (alg, typ) and headers returned from
        the :meth:`~flask_jwt_extended.JWTManager.additional_headers_loader`
        callback. On conflict, these headers take precedence.

    :return:
        An encoded access token
    """
    jwt_manager = get_jwt_manager()
    return jwt_manager._encode_jwt_from_config(
        claims=additional_claims,
        expires_delta=expires_delta,
        fresh=fresh,
        headers=additional_headers,
        identity=identity,
        token_type="access",
    )